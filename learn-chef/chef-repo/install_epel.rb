bash 'install_epel' do
  user 'root'
  cwd '/tmp'
  code <<-EOH
  yum install http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm -y
  EOH
end
  
