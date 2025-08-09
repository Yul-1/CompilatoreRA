# Risk Assessment

**Obiettivo**: Identificare e mitigare i rischi di sicurezza del nuovo server e-commerce per conformità PCI-DSS e GDPR.
**Ambito**: Server Debian 12 con Nginx, MariaDB, e applicativo Magento.

---
## Tabella dei Rischi

| ID Rischio   | Asset/Vulnerabilit�   |   Probabilit� (1-5) |   Impatto (1-5) |   Punteggio | Livello Rischio   | Azione Raccomandata                                                                                                                     |
|--------------|-----------------------|---------------------|-----------------|-------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| RISK-001     | Database Utenti       |                   5 |               5 |          25 | CRITICO           | Imporre password robuste e politiche di rotazione.                                                                                      |
| RISK-002     | Web Application       |                   4 |               5 |          20 | CRITICO           | Implementare validazione e sanitizzazione degli input.                                                                                  |
| RISK-003     | Server Web            |                   5 |               4 |          20 | CRITICO           | Applicare regolarmente patch e aggiornamenti di sicurezza.                                                                              |
| RISK-004     | Backup Dati           |                   4 |               4 |          16 | ALTO              | Cifrare e testare regolarmente i backup.                                                                                                |
| RISK-005     | Configurazione SSH    |                   4 |               4 |          16 | ALTO              | Disabilitare l'accesso root da SSH, impostare regole per indirizzi permessi, usare una chiave ellittica, cambiare la porta predefinita. |

## Piano di Trattamento del Rischio


### RISK-001 - Database Utenti

**Livello rischio**: CRITICO
**Trattamento**: Mitigare

L'utilizzo di password deboli o predefinite espone il database utenti a rischi di accesso non autorizzato.
 [cite:RISK-001]

**Piano di Mitigazione:**
1. Impostare requisiti minimi di complessità per le password.
2. Forzare la rotazione periodica delle password.
3. Bloccare gli account dopo tentativi falliti ripetuti.
4. Monitorare e loggare i tentativi di accesso.
 [cite:RISK-001]

### RISK-002 - Web Application

**Livello rischio**: CRITICO
**Trattamento**: Mitigare

L'assenza di validazione degli input permette ad un attaccante di eseguire codice malevolo o accedere a dati sensibili.
 [cite:RISK-002]

**Piano di Mitigazione:**
1. Validare tutti gli input lato server e client.
2. Utilizzare whitelist per i dati accettati.
3. Applicare escaping e sanitizzazione dove necessario.
4. Eseguire test di sicurezza periodici.
 [cite:RISK-002]

### RISK-003 - Server Web

**Livello rischio**: CRITICO
**Trattamento**: Mitigare

La mancata applicazione di aggiornamenti di sicurezza espone il server a vulnerabilità note e facilmente sfruttabili.
 [cite:RISK-003]

**Piano di Mitigazione:**
1. Monitorare i bollettini di sicurezza dei software utilizzati.
2. Automatizzare il processo di aggiornamento dove possibile.
3. Testare gli aggiornamenti in ambiente di staging prima della produzione.
4. Documentare le attività di patching.
 [cite:RISK-003]

### RISK-004 - Backup Dati

**Livello rischio**: ALTO
**Trattamento**: Mitigare

Backup non cifrati o non testati possono portare a perdita di dati o accessi non autorizzati in caso di incidente.
 [cite:RISK-004]

**Piano di Mitigazione:**
1. Utilizzare algoritmi di cifratura robusti per i backup.
2. Eseguire test di ripristino periodici.
3. Limitare l'accesso ai backup solo al personale autorizzato.
4. Documentare le procedure di backup e ripristino.
 [cite:RISK-004]

### RISK-005 - Configurazione SSH

**Livello rischio**: ALTO
**Trattamento**: Mitigare

Le configurazioni SSH standard aumentano significativamente la probabilità di successo per un attaccante.
Il server risulta esposto su porta 22 con configurazioni predefinite che facilitano attacchi brute force e 
compromissioni del sistema.
 [cite:RISK-005]

**Piano di Mitigazione:**
È buona pratica eseguire un backup delle configurazioni critiche:
`sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup.$(date +%Y%m%d_%H%M%S)`

Creare una coppia di chiavi di autenticazione ellittiche (Ed25519):
`sudo mkdir -p /etc/ssh/hardened_keys`
`sudo ssh-keygen -t ed25519 -f /etc/ssh/hardened_keys/ssh_host_ed25519_key -N ""`

Creare un banner di avvertimento legale:
`sudo nano /etc/ssh/ssh_banner.txt`

Aprire il file di configurazione `sudo nano /etc/ssh/sshd_config` e apportare le seguenti modifiche:
* Cambio porta da 22 a 2222.
* Disabilitare il root login.
* Restrizioni di accesso solo ad utenti permessi.
* Indicare il path per le chiavi ellittiche e il banner.
* Impostare soluzioni di hardening (limite tentativi, sessioni, etc.).
* Abilitare logging verbose.

Verificare la correttezza della sintassi:
`sudo sshd -t`

Riavviare il servizio SSH:
`sudo systemctl reload ssh`

Una volta verificato il funzionamento, rimuovere la regola per la vecchia porta:
`sudo ufw delete allow 22/tcp`

Per un'ulteriore protezione, installare e configurare fail2ban per bloccare tentativi di accesso falliti. [cite:RISK-005]



## Rischio Residuo
(Testo standard sul rischio residuo...)


## Considerazioni ulteriori e best practice
(Testo standard sulle best practice...)

**Data**: 08/08/2025
**Autore**: Andrea Emanuele Peluso