#
# Cookbook Name:: learn_chef_httpd
# Recipe:: default
#
# Copyright (c) 2017 The Authors, All Rights Reserved.

package 'httpd' do
  action :install
end

service 'httpd' do
  action [:enable, :start]
end

group 'web_admin' do
  action :create
end

user 'web_admin' do
  action :create
  group 'web_admin'
  system true
  shell '/bin/bash'
end

template '/var/www/html/index.html' do
  action :create
  source 'index.html.erb'
  mode '0644'
  owner 'web_admin'
  group 'web_admin'
end
