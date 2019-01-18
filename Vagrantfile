# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
 config.vm.box_url = "https://download.fedoraproject.org/pub/fedora/linux/releases/29/Cloud/x86_64/images/Fedora-Cloud-Base-Vagrant-29-1.2.x86_64.vagrant-libvirt.box"
 config.vm.box = "f29-cloud-libvirt"


 # Create a forwarded port mapping which allows access to a specific port
 # within the machine from a port on the host machine. In the example below,
 # accessing "localhost:8080" will access port 80 on the guest machine.
 config.vm.network "forwarded_port", guest: 8000, host: 8000
# config.vm.network "forwarded_port", host: 9001, guest: 9001

 # This is an optional plugin that, if installed, updates the host's /etc/hosts
 # file with the hostname of the guest VM. In Fedora it is packaged as
 # ``vagrant-hostmanager``
 if Vagrant.has_plugin?("vagrant-hostmanager")
     config.hostmanager.enabled = true
     config.hostmanager.manage_host = true
 end

 # Vagrant can share the source directory using rsync, NFS, or SSHFS (with the vagrant-sshfs
 # plugin). Consult the Vagrant documentation if you do not want to use SSHFS.
 config.vm.synced_folder ".", "/vagrant", disabled: true
# config.vm.synced_folder ".", "/home/vagrant/project", 
#    ssh_opts_append: "-o IdentitiesOnly=true",
#    sshfs_opts_append: "-o nonempty",
#    type: "sshfs"

 # To cache update packages (which is helpful if frequently doing `vagrant destroy && vagrant up`)
 # you can create a local directory and share it to the guest's DNF cache. Uncomment the lines below
 # to create and use a dnf cache directory
 
 Dir.mkdir('.dnf-cache') unless File.exists?('.dnf-cache')
 config.vm.synced_folder ".dnf-cache", "/var/cache/dnf",
    ssh_opts_append: "-o IdentitiesOnly=true",
#    sshfs_opts_append: "-o nonempty",
    type: "sshfs"

 # Comment this line if you would like to disable the automatic update during provisioning
# config.vm.provision "shell", inline: "sudo dnf upgrade -y"

 # bootstrap and run with ansible
 config.vm.provision "shell", inline: "sudo dnf -y install libselinux-python"
 config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/vagrant-playbook.yml"
 end


 # Create the box
 config.vm.define "taiga_F29" do |host|
    host.vm.host_name = "f29test.example.com"

    host.vm.provider :libvirt do |domain|
        # Season to taste
        domain.cpus = 4
        domain.graphics_type = "spice"
        # The unit tests use a lot of RAM.
        domain.memory = 4096
        domain.video_type = "qxl"

        # Uncomment the following line if you would like to enable libvirt's unsafe cache
        # mode. It is called unsafe for a reason, as it causes the virtual host to ignore all
        # fsync() calls from the guest. Only do this if you are comfortable with the possibility of
        # your development guest becoming corrupted (in which case you should only need to do a
        # vagrant destroy and vagrant up to get a new one).
        #
        # domain.volume_cache = "unsafe"
    end
 end
end
