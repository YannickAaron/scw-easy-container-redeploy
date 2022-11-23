# scw-easy-container-redeploy
Simple action using the Scaleway api to redeploy a container by providing the container name.

## Prerequisites
You will need a scaleway account and a token to use this action. You can find more information about how to create a token [here](https://www.scaleway.com/en/docs/generate-api-token/).

## Usage
Please make sure to use the latest version of this action. You can find the latest version [here](https://github.com/marketplace/actions/scw-easy-container-redployment)

```yml
      - name: redeploy scw - container
        uses: YannickAaron/scw-easy-container-redeploy@0.22
        with:
          api_secret_key: ${{ secrets.SCALEWAY_API_SECRET_KEY }}
          container_name: 'my-container'
```

**Full Example:**

The following example shows how this action can be used to automatically build a container, push it to the registry and redeploy it on the server, all using [scaleway](https://www.scaleway.com/) with github actions.

```yml
name: deploy

# Controls when the workflow will run
on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      uses: actions/checkout@v2
    - name: login to scaleway docker registry
      uses: docker/login-action@v1
      with:
        registry: ${{ secrets.CONTAINER_REG_ENDPOINT}}
        username: nologin
        password: ${{ secrets.SCW_SECRET_KEY }}
    - name: build docker container
      run: docker build . -t ${{ secrets.CONTAINER_REG_ENDPOINT}}/<your-container-name>
    - name: push docker container
      run: docker push ${{ secrets.CONTAINER_REG_ENDPOINT}}/<your-container-name>
    - name: redeploy scw - container
      uses: YannickAaron/scw-easy-container-redeploy@0.22
      with:
        api_secret_key: ${{ secrets.SCW_SECRET_KEY }}
        container_name: '<your-container-name>'
```

## Inputs
| Name | Description | Required | Default |
| --- | --- | --- | --- |
| api_secret | The api secret key of your scaleway account. | ✔️ | |
| container_name | The name of the container you want to redeploy. | ✔️ | |
| region | The region to use for the api calls | ❌ | fr-par |
| organization_id | The organization id of your scaleway account. | ❌ | |
| project_id | The project id of your scaleway account. | ❌ | |
| api_version | The api version of the scaleway api. | ❌ | v1beta1 |

## License
MIT License
@YannickAaron

