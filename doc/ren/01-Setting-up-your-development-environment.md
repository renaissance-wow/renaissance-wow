# Setting up your development environment

## First time setup

### Install Docker

First, you'll need to install docker from https://docs.docker.com/get-docker/.
Choose the option that best fits your operating system. You'll likely need to
restart your system after installing Docker, so if the installer prompts you to
do so, please do.

Docker is "container runtime", which is a fancy way of saying -- you can build,
experiment, and test changes in an environment isolated, without cluttering or
potentially breaking your system.

### Install Git

Next, you'll need to install git. If you're on Windows machine, you should
install `git-bash`, as it'll make your life a lot easier while working on the
project. You'll be running quite a few commands in this application, so make
sure you pin it someplace you can find it easily. 
**For the remainder of this tutorial, git-bash will be referred to as the terminal**

If you're on a Unix-like or BSD-like system, such as MacOS, Debian, or Fedora,
you should use your system's respective package manager to install git if it
isn't already (`brew`, `apt`, or `dnf`, resectively).

Git is a source version control application, which makes it easy for developers
to work on the same project simultaneously and asynchronously.

### Building the Project 

1. Clone the Azeroth-Core git repository by running the following 

    ```bash
    git clone https://github.com/azerothcore/azerothcore-wotlk.git
    ```

1. Compile the core

    Make sure that Docker is running. On Windows, you'll need to launch the
    `Docker Desktop` app. On *nix systems, you should run `sudo systemctl start dockerd`.

    **If you're building the core for the first time, or are building the core**
    **for production, you should run the following:**

        ```bash
        cd azerothcore-wotlk  # change directory into the git repository you just downloaded.
        ./acore.sh docker build
        ```

        This can take a pretty long time, but you'll only have to do this once.

    
    **If you are developing against the core, and need a fast way to build and**
    **test changes, use the following command:**
    ```bash
    ./acore.sh docker dev:build
    ```

1. Download the client data

    **IMPORTANT** : This command should be executed only at the first
    installation and when there's a new version of the client-data available

    ```bash
    ./acore.sh docker client-data
    ```



## Post-setup

### Run the container
Use the following command to start the a container running the core:

```bash
./acore.sh docker start:app:d
```

This will start a docker container containing the entire core. The `:d` postfix
indicates that the container will run in *detatched* mode, meaning it'll run the
container as a background service.

### Attach to AC-bash 

Next, you'll need to attach to the detached container. We'll do this by locating
the random hash associated with the worldserver container. In your terminal, run:

```bash
docker container ls
```

The Docker daemon will respond with a list of running containers. Locate the worldserver container:

```bash
CONTAINER ID   IMAGE                                     COMMAND                  CREATED             STATUS                    PORTS                                            NAMES
92f2743ed34a   acore/ac-wotlk-worldserver-local:master   "./acore.sh run-worl…"   About an hour ago   Up 53 minutes             0.0.0.0:7878->7878/tcp, 0.0.0.0:8085->8085/tcp   azerothcore-wotlk-ac-worldserver-1
97bd0d767743   acore/ac-wotlk-authserver-local:master    "./acore.sh run-auth…"   About an hour ago   Up 53 minutes             0.0.0.0:3724->3724/tcp                           azerothcore-wotlk-ac-authserver-1
7a34d1f3aee5   mysql:8.0                                 "docker-entrypoint.s…"   About an hour ago   Up 53 minutes (healthy)   0.0.0.0:3306->3306/tcp, 33060/tcp                azerothcore-wotlk-ac-database-1
```

It looks like our worldserver's `CONTAINER ID` begins with `92f`. We don't need
to copy the whole container identifier, just enough for the container to be
identified from the rest of the running containers. Run the command below, replacing 
`92f` with the beginning of the container id for your running worldserver.

```
docker attach 92f
```

Now that you've attached yourself to the running worldserver, you should see the
`AC>` cursor in your terminal. Congratulations, you've successfully hacked the
mainframe! Just kidding, but you **did** attach yourself to the shell of the
running the worldserver container.

### Create an admin account

After attaching to the worldserver container, you'll need to create an account.
Use the following command to do so.

```bash
AC> account create <user> <pass>
```

# level -> Role name
# 0     -> SEC_PLAYER
# 1     -> SEC_MODERATOR
# 2     -> SEC_GAMEMASTER
# 3     -> SEC_ADMINISTRATOR

Finally, set the newly created account as an administrator. This will give you access to
[these commands](https://www.azerothcore.org/wiki/gm-commands) while in-game.

```bash
AC> account set gmlevel <user> <level> <realm; -1 for all realms>
```
