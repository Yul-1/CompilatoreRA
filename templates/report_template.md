# Risk Assessment

**Obiettivo**: {{ project.objective }}
**Ambito**: {{ project.scope }}

---
## Tabella dei Rischi

| ID Rischio | Asset/Vulnerabilità | Probabilità (1-5) | Impatto (1-5) | Punteggio | Livello Rischio | Azione Raccomandata |
|---|---|---|---|---|---|---|
{% for risk in risks %}
| {{ risk.risk_id }} | {{ risk.asset }} | {{ risk.probability }} | {{ risk.impact }} | {{ risk.score }} | **{{ risk.level }}** | {{ risk.mitigation.summary }} |
{% endfor %}

---
## Piano di Trattamento del Rischio

{% for risk in risks %}
### {{ risk.risk_id }} - {{ risk.asset }}

**Livello rischio**: {{ risk.level }}
**Trattamento**: {{ risk.mitigation.treatment }}

{{ risk.justification }}

**Piano di Mitigazione:**
{{ risk.mitigation.steps }}
---
{% endfor %}

## Rischio Residuo
(Testo standard sul rischio residuo...) [cite_start][cite: 532, 533, 534, 535, 536, 537, 538, 539]

## Considerazioni ulteriori e best practice
(Testo standard sulle best practice...) [cite_start][cite: 541, 542, 543, 544, 545, 546, 547, 548, 549, 550]

---
**Data**: {{ project.date }}
**Autore**: {{ project.author }}