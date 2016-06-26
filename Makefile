provision:
	ansible-playbook -i /etc/ansible/hosts -s -u ubuntu ansible/provision.yml -vvvv

deploy:
	ansible-playbook -i /etc/ansible/hosts -s -u ubuntu ansible/deploy.yml -vvvv