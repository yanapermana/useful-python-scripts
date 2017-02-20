import docker
client = docker.from_env()

# run a container
client.containers.run("ubuntu", "echo hello world")

client.containers.list()

container = client.containers.get('45e6d2de7c54')

pid = container.attrs['State']['Pid']
