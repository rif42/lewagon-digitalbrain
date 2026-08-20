---
type: notion-import
notion-id: e2cec1fdd5ee43e4aeefb506dc9f81c1
source-url: https://app.notion.com/p/lewagon/Jupyter-Hub-Notice-e2cec1fdd5ee43e4aeefb506dc9f81c1
imported: 2026-07-21
---
# Jupyter Hub Notice
> [!video] https://www.notion.com/help/images-files-and-media
# Hosting
### Jupyter Hub
Our self-hosted Jupyter Hub solution relies on <https://z2jh.jupyter.org/en/stable/> which consists of a Kubernetes cluster. The underlying architecture is described in [The JupyterHub Architecture](https://z2jh.jupyter.org/en/stable/administrator/architecture.html).
### Scaleway
Our Kubernetes clusters are hosted on [Scaleway](https://www.scaleway.com/), a French cloud provider founded by Xavier Niel in 1999.
- cerfied **ISO/IEC 27001:2022** ([certificat](https://www-uploads.scaleway.com/IS_787020_EN_46136c6c21.pdf))
- GDPR compliance engagement [Data Processing Agreement](https://www-uploads.scaleway.com/Data_Processing_Agreement_03092021_6e2ca4da3c.pdf)
- More information security-wise <https://www.scaleway.com/en/security-and-resilience/>
# Ephemeral clusters
### One hub for one training
For each training, we instantiate a dedicated Jupyter Hub associated to a subdomain w/ the name of the entity and the number of the training, e.g. for CA-Indosuez batch #1 it would be [cais-1.jupyterhub.lewagon.io/](https://cais-1.jupyterhub.lewagon.io/).
Learners get a dedicated container spawned automatically by onboarding on the Jupyter Hub through their [learn.lewagon.com](http://learn.lewagon.com/) enrollment, providing them w/ an isolated [Jupyter Lab](https://jupyter.org/try). They can sign out of the lab and re-connect anytime without losing their work.
By default, the cluster is terminated after the end of the training, deleting any associated resources.
### Whitelisting IPs
If the training takes place within your offices, you can provide us with a list of IP addresses or range of addresses that we can allow explicitly, preventing the hub from being accessed outside your facilities.
## Related
- [[Onboarding]]
