$setup = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get update
SCRIPT

$dependencies = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get install python-software-properties -y
    DEBIAN_FRONTEND=noninteractive echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
    DEBIAN_FRONTEND=noninteractive echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections
    DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:webupd8team/java && apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql libpq-dev oracle-java7-installer curl
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev libjpeg-dev zlib1g-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-virtualenv virtualenvwrapper make
    DEBIAN_FRONTEND=noninteractive wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.5.1.deb
    DEBIAN_FRONTEND=noninteractive dpkg -i elasticsearch-1.5.1.deb
    DEBIAN_FRONTEND=noninteractive service elasticsearch start
    DEBIAN_FRONTEND=noninteractive pip install -r /vagrant/requirements.txt
SCRIPT

Vagrant.configure('2') do |config|

    config.vm.box = 'precise64'
    config.vm.box_url = "http://files.vagrantup.com/" + config.vm.box + ".box"

    config.ssh.forward_agent = true
    # Forward the dev server port
    config.vm.network :forwarded_port, host: 8000, guest: 8000

    config.vm.provision "shell", inline: $setup
    config.vm.provision "shell", inline: $dependencies
end
