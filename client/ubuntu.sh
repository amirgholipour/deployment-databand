
# create an alias for Python
sudo apt update -y
sudo apt upgrade -y
echo "alias python=python3" >> $HOME/.bash_aliases 
. $HOME/.bash_aliases 

# Install pip
sudo apt install python3-pip -y

# Install Jupyter Notebooks
sudo apt install jupyter -y
pip install --upgrade jupyter_core
pip install jupyterlab
pip install bash_kernel
python3 -m bash_kernel.install

. $HOME/.profile

# Install snap
sudo snap install yq

# Install helm
sudo snap install helm --classic

# Install oc 
wget https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/4.10.54/openshift-client-linux-4.10.54.tar.gz
tar -zxf openshift-client-linux-4.10.54.tar.gz
sudo mv kubectl oc /usr/local/bin
rm README.md openshift-client-linux-4.10.54.tar.gz

# Install docker
sudo apt-get install ca-certificates curl gnupg
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
sudo usermod -aG docker $USER

# Install additional modules for python DAGs
pip install psycopg2-binary
pip install pandas
pip install sqlalchemy
pip install dbnd
# only if you get errors during the execution of the python dags
# pip install markupsafe==2.0.1

# Start Jupyter

jupyter lab --ip 0.0.0.0 --port 8080 --notebook-dir ~/deployment-databand  --no-browser & disown