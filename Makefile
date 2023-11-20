publish:
	mkdocs build
	mkdocs gh-deploy
	del site