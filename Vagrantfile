# -*- mode: ruby -*-
# vi: set ft=ruby ts=2 sw=2 expandtab :

UID = Process.euid

PROJECT_DIR="/vagrant"
BUILD_SCRIPTS="#{PROJECT_DIR}/build_scripts"

CASSANDRA_POOL="cassandra"
VIRTUAL_ENV_PATH="/tmp/virtual_env27"
KEY_SPACE="KeySpace"
COLUMN_FAMILY="ColumnFamily"

PROJECT = "tornado-pycassa-cassandra"

ENV['VAGRANT_NO_PARALLEL'] = 'yes'
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'docker'
VAGRANTFILE_VERSION = "2"
Vagrant.configure(VAGRANTFILE_VERSION) do |config|

  config.vm.define "cassandra" do |app|
    app.vm.provider "docker" do |d|
      d.image = "jean553/docker-cassandra"
      d.name = "#{PROJECT}_cassandra"
    end
  end

  environment_variables = {
      "HOST_USER_UID" => UID,

      # for provisioning
      "VIRTUAL_ENV_PATH" => VIRTUAL_ENV_PATH,
      "ENV_NAME" => "devdocker",
      "BUILD_SCRIPTS" => BUILD_SCRIPTS,
      "APP_NAME" => PROJECT,
      "APP_PATH" => PROJECT_DIR,

      # for the app
      "CASSANDRA_POOL" => CASSANDRA_POOL,
      "KEY_SPACE" => KEY_SPACE,
      "COLUMN_FAMILY" => COLUMN_FAMILY,
  }

  config.ssh.insert_key = true
  config.vm.define "dev", primary: true do |app|
    app.vm.provider "docker" do |d|
      d.image = "allansimon/allan-docker-dev-python"
      d.name = "#{PROJECT}_dev"
      d.link "#{PROJECT}_cassandra:cassandra"
      d.has_ssh = true
      d.env = environment_variables
    end
    app.ssh.username = "vagrant"

    app.vm.network "forwarded_port", guest: 8080, host: 8080

    app.vm.provision "ansible", type: "shell" do |ansible|
      ansible.env = environment_variables
      ansible.inline = "
        set -e
        cd $APP_PATH
        ansible-playbook bootstrap.yml
        echo 'done, you can now run `vagrant ssh`'
      "
    end
  end
end
