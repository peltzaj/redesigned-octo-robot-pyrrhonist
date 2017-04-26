directory '/tmp/messages' do
  action :create
end 

file '/tmp/messages/motd' do
  action :create
  content 'all the world'
end

