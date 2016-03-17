deploy:
	ansible-playbook -i /etc/ansible/hosts -s -u ubuntu ansible/provision.yml