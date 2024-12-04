# How Enabling Organization Members to use Personal Access Tokens

## Here are caveats and alternatives to using Personal Access Tokens (tokens)
These tokens are purely to enable an individual to authenticate with GitHub. A token (a text string
) is a password with restricted use and can be revoked. Nevertheless there are caveats and alternatives. Most importantly, do not check in these tokens - they should remain on your physical machines / VM's.

[Direct quote from 
`https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens`]

### Keeping your personal access tokens secure
Personal access tokens are like passwords, and they share the same inherent security risks. Before creating a new personal access token, consider if there is a more secure method of authentication available to you:

To access GitHub from the command line, you can use GitHub CLI or Git Credential Manager instead of creating a personal access token.
When using a personal access token in a GitHub Actions workflow, consider whether you can use the built-in GITHUB_TOKEN instead. For more information, see "Automatic token authentication."
If these options are not possible, and you must create a personal access token, consider using another CLI service to store your token securely.

When using a personal access token in a script, you can store your token as a secret and run your script through GitHub Actions. For more information, see "Using secrets in GitHub Actions." You can also store your token as a Codespaces secret and run your script in Codespaces. For more information, see "Managing your account-specific secrets for GitHub Codespaces."

For more information about best practices, see "Keeping your API credentials secure."
*End quote*

## Set organization policy to allow members tokens
https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization
- Enable fine grained tokens (not "class" which is deprecated)
- Set other parameters like token expiry time

## Add person to organization
`https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization`
- Person will get an email invite

# Add a contributor to the specific project
https://github.com/orgs/community/discussions/62375
- Pick their type of access (read/triage/write/maintain/admin)
- Contributor will get a notification to accept the invite

## Create token
`https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/managing-requests-for-personal-access-tokens-in-your-organization`

Each person creates their own token. Follow instructions here, under topic "Creating a fine-grained personal access token":
`https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens]`
