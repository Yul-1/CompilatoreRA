# compiler.py
import yaml
from jinja2 import Environment, FileSystemLoader
import subprocess
import sys

def calculate_risk_level(score):
    """Calcola il livello di rischio basandosi sul punteggio."""
    if score >= 20:
        return "CRITICO"  # [cite: 19]
    elif 13 <= score <= 19:
        return "ALTO"  # [cite: 19]
    elif 8 <= score <= 12:
        return "MEDIO"  # [cite: 19]
    else:
        return "BASSO"  # [cite: 19]

def main(project_file):
    """Funzione principale per compilare il report."""
    
    # 1. Carica il file di configurazione del progetto
    with open(project_file, 'r') as f:
        project_data = yaml.safe_load(f)

    processed_risks = []
    # 2. Processa ogni rischio definito nel progetto
    for risk_ref in project_data.get('risks', []):
        risk_id = risk_ref['id']
        
        # Carica i dati completi del rischio dalla knowledge base
        try:
            with open(f'risks_db/{risk_id}.yml', 'r') as f:
                risk_data = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"ATTENZIONE: File per {risk_id} non trovato in risks_db/. Salto.")
            continue
            
        # Aggiungi i dati specifici del progetto (P e I)
        risk_data['probability'] = risk_ref['probability']
        risk_data['impact'] = risk_ref['impact']
        
        # 3. Calcola Punteggio e Livello
        risk_data['score'] = risk_data['probability'] * risk_data['impact']
        risk_data['level'] = calculate_risk_level(risk_data['score'])
        
        processed_risks.append(risk_data)
        
    # Ordina i rischi per punteggio, dal più alto al più basso
    processed_risks.sort(key=lambda r: r['score'], reverse=True)

    # 4. Genera il documento usando il template Jinja2
    env = Environment(loader=FileSystemLoader('templates/'))
    template = env.get_template('report_template.md')
    
    output_content = template.render(
        project=project_data,
        risks=processed_risks
    )
    
    # 5. Salva il file Markdown di output
    output_filename_md = f"{project_data['project_name'].replace(' ', '_')}.md"
    with open(output_filename_md, 'w') as f:
        f.write(output_content)
        
    print(f"Report generato con successo: {output_filename_md}")
    
    # 6. (Opzionale) Converte automaticamente in PDF usando Pandoc
    output_filename_pdf = f"{project_data['project_name'].replace(' ', '_')}.pdf"
    try:
        subprocess.run(['pandoc', output_filename_md, '-o', output_filename_pdf, '--pdf-engine=xelatex'], check=True)
        print(f"PDF generato con successo: {output_filename_pdf}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nConversione in PDF fallita. Assicurati che Pandoc e un motore LaTeX (es. MiKTeX, TeX Live) siano installati.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Uso: python compiler.py <percorso_file_progetto.yml>")