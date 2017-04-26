# See http://docs.chef.io/config_rb_knife.html for more information on knife configuration options

current_dir = File.dirname(__FILE__)
log_level                :info
log_location             STDOUT
node_name                "admin"
client_key               "#{current_dir}/admin.pem"
chef_server_url          "https://chef-server.test/organizations/4thcoffee"
cookbook_path            ["#{current_dir}/../cookbooks"]

# Amazon AWS
# knife[:aws_access_key_id] = ENV['AWS_ACCESS_KEY_ID']
# knife[:aws_secret_access_key] = ENV['AWS_SECRET_ACCESS_KEY']

# Rackspace Cloud
# knife[:rackspace_api_username] = ENV['RACKSPACE_USERNAME']
# knife[:rackspace_api_key] = ENV['RACKSPACE_API_KEY']
