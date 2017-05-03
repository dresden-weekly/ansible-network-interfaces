DIR := ${CURDIR}

test:
	docker run --rm -ti -v$(DIR):/ansible-network-interfaces \
	-e "PATH=/ansible-network-interfaces/vendor/bin/:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" \
	-e "PYTHONUSERBASE=/ansible-network-interfaces/vendor" \
	python:3 /ansible-network-interfaces/tests/run.sh
