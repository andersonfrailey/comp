
dist-build:
	# template command:
	# docker build --no-cache --build-arg TAG=$(TAG) -t comp/{project_name}_tasks:$(TAG) --file dockerfiles/projects/Dockerfile.{project_name}_tasks ./

	cd distributed && \
	docker build -t comp/distributed:$(TAG) ./ -f dockerfiles/Dockerfile && \
	docker build --build-arg TAG=$(TAG) -t comp/flask:$(TAG) --file dockerfiles/Dockerfile.flask ./ && \
	docker build --build-arg TAG=$(TAG) -t comp/celerybase:$(TAG) --file dockerfiles/Dockerfile.celerybase ./ && \
	docker build --build-arg TAG=$(TAG) -t comp/compbaseball_tasks:$(TAG) --file dockerfiles/projects/Dockerfile.compbaseball_tasks ./ && \
	docker build --build-arg TAG=$(TAG) -t comp/taxbrain_tasks:$(TAG) --file dockerfiles/projects/Dockerfile.taxbrain_tasks ./

dist-push:
	cd distributed && \
	docker push comp/distributed:$(TAG) && \
	docker push comp/flask:$(TAG) && \
	docker push comp/celerybase:$(TAG) && \
	docker push comp/compbaseball_tasks:$(TAG) && \
	docker push comp/taxbrain_tasks:$(TAG)

dist-test:
	cd distributed && \
	docker-compose rm -f && \
	docker-compose run flask py.test -s -v && \
	docker-compose rm -f

webapp-build:
	docker build -t comp/web:$(TAG) ./

webapp-push:
	docker tag comp/web:$(TAG) registry.heroku.com/compmodels/web
	docker push registry.heroku.com/compmodels/web

webapp-test-push:
	docker tag comp/web:$(TAG) registry.heroku.com/compmodels-test/web
	docker push registry.heroku.com/compmodels-test/web

webapp-release:
	heroku container:release web -a compmodels

webapp-test-release:
	heroku container:release web -a compmodels-test
