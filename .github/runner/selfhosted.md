

# Self hosted runner un linux

# install tools 


## pipx 
```bash
sudo apt update
# pipx
sudo apt install pipx
pipx ensurepath
``` 

# install 
https://docs.github.com/en/actions/hosting-your-own-runners

- Install self hosted runner 
- Configure environment 
> `.../actions_runner/.env`
```
# Add 
LANG=en_US.UTF-8
AGENT_TOOLSDIRECTORY=/home/jos/actions-runner/_tools
```
- [check if additional permissions are needed](https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#linux)
- testrun 
- configure to run as a service 
- start service 



