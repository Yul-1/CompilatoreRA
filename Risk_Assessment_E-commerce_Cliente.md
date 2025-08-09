# Risk Assessment

**Obiettivo**: Identificare e mitigare i rischi di sicurezza del nuovo server e-commerce per conformit√† PCI-DSS e GDPR.
**Ambito**: Server Debian 12 con Nginx, MariaDB, e applicativo Magento.

---
## Tabella dei Rischi

| ID Rischio | Asset/Vulnerabilit‡ | Probabilit‡ (1-5) | Impatto (1-5) | Punteggio | Livello Rischio | Azione Raccomandata |
|---|---|---|---|---|---|---|

| RISK-005 | Configurazione SSH | 4 | 4 | 16 | **ALTO** | Disabilitare l'accesso root da SSH, impostare regole per indirizzi permessi, usare una chiave ellittica, cambiare la porta predefinita. |


---
## Piano di Trattamento del Rischio


### RISK-005 - Configurazione SSH

**Livello rischio**: ALTO
**Trattamento**: Mitigare

Le configurazioni SSH standard aumentano significativamente la probabilit√† di successo per un attaccante.
Il server risulta esposto su porta 22 con configurazioni predefinite che facilitano attacchi brute force e 
compromissioni del sistema.


**Piano di Mitigazione:**
√à buona pratica eseguire un backup delle configurazioni critiche:
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

Per un'ulteriore protezione, installare e configurare fail2ban per bloccare tentativi di accesso falliti.
---


## Rischio Residuo
(Testo standard sul rischio residuo...) [cite_start][cite: 532, 533, 534, 535, 536, 537, 538, 539]

## Considerazioni ulteriori e best practice
(Testo standard sulle best practice...) [cite_start][cite: 541, 542, 543, 544, 545, 546, 547, 548, 549, 550]

---
**Data**: 08/08/2025
**Autore**: Andrea Emanuele Peluso