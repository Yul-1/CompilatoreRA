# Risk Assessment

**Obiettivo**: {{ project.objective }}
**Ambito**: {{ project.scope }}

---
## Tabella dei Rischi

{{ risks_table_md }}

## Piano di Trattamento del Rischio

{% for risk in risks %}
### {{ risk.risk_id }} - {{ risk.asset }}

**Livello rischio**: {{ risk.level }}
**Trattamento**: {{ risk.mitigation.treatment }}

{{ risk.justification }}

**Piano di Mitigazione:**
{{ risk.mitigation.steps }}
{% endfor %}


## Rischio Residuo
(Testo standard sul rischio residuo...)


## Considerazioni ulteriori e best practice
(Testo standard sulle best practice...)

**Data**: {{ project.date }}
**Autore**: {{ project.author }}