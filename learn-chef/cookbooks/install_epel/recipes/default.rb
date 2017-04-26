#
# Cookbook:: install_epel
# Recipe:: default
#
# Copyright:: 2017, The Authors, All Rights Reserved.
bash 'install_epel' do
  user 'root'
  cwd '/tmp'
  code <<-EOH
  wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm
  yum install epel-release-7-9.noarch.rpm -y
  rm -f /tmp/epel-release-7-9.noarch.rpm
  EOH
end
  
