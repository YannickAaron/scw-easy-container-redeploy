# scw-easy-container-redeploy
Simple action using the Scaleway api to redeploy a container by providing the container name.

## Prerequisites
You will need a scaleway account and a token to use this action. You can find more information about how to create a token [here](https://www.scaleway.com/en/docs/generate-api-token/).

## Usage
Please make sure to use the latest version of this action. You can find the latest version [here](https://github.com/marketplace/actions/scw-easy-container-redployment)

```yml
      - name: redeploy scw - container
        uses: YannickAaron/scw-easy-container-redeploy@0.1
        with:
          api_secret_key: ${{ secrets.SCALEWAY_API_SECRET_KEY }}
          container_name: 'my-container'
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

