## Best CI practices

## Github actions CI

# Keep your Actions minimal

Simpler actions would require less time waisted on waiting.

Github provides 2000 hours limited plan. For personal use it is enough but in team projects and big repositories this could be a problem and less time workflow takes more times it can be started.

# Don’t install dependencies unnecessarily

Continuing previous step. Installing packages requires time.

# Never hardcode secrets

There is a better way to store passwords and key. Github secrets are stored in repository under encryptions which ensures its safety.

## Jenkins CI

# Keep Jenkins Secure At All Times

Informs the Jenkins environment as to which users and/or groups can access which aspects of Jenkins, and to what extent.

# Always Backup The “JENKINS_HOME” Directory

This requires you to manually start it to back up your data.

# Maintain Higher Test Code Coverage & Run Unit Tests As Part Of Your Pipeline
