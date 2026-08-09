# Download statistics setup

The notebooks in this folder query the public PyPI download dataset in BigQuery:

1. `1-update_stats.ipynb` collects every completed month after the latest month in `downloads.csv`.
2. `2-report-stats.ipynb` regenerates the charts from the CSV.

The updater uses Google Application Default Credentials (ADC). Use your Google user account for local development. Do not create or download a service-account JSON key.

## Requirements

- A Google account.
- A Google Cloud project used to run and account for BigQuery query jobs.
- The Google Cloud CLI (`gcloud`, including the bundled `bq` tool).
- `uv` for the Python environment.

Select or create a project in the [Google Cloud project selector](https://console.cloud.google.com/projectselector2/home/dashboard). Note its project ID, which is not always the same as its display name.

For a project owned by someone else, the user needs:

- **BigQuery Job User** (`roles/bigquery.jobUser`) to run query jobs.
- Permission `serviceusage.services.use` to use the project for quota. Project Owner and Editor include this permission; an administrator can grant a narrower custom role if needed.

Access to the public PyPI table does not require BigQuery Data Viewer on your own project. BigQuery Admin is not required. Review [BigQuery pricing and the free usage tier](https://cloud.google.com/bigquery/pricing) before collecting a long backlog. A monthly query currently scans roughly 1-2 GB, but this can change as the public dataset grows.

## Install the Google Cloud CLI

Use Google's current [installation guide](https://cloud.google.com/sdk/docs/install-sdk) when setting up a new machine. It supplies the appropriate current version and supported Python runtime.

### Windows

Download and run Google's signed [Google Cloud CLI installer](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe). Keep the bundled Python option enabled unless there is a reason to manage it separately. Open a new PowerShell terminal after installation.

### macOS

Use the macOS section of Google's [installation guide](https://cloud.google.com/sdk/docs/install-sdk#mac). Choose the ARM64 archive for Apple silicon or the x86_64 archive for an Intel Mac, extract it, and run `google-cloud-sdk/install.sh`. Open a new terminal after allowing the installer to update `PATH`.

### Linux

Choose the archive matching `uname -m` in Google's [Linux installation guide](https://cloud.google.com/sdk/docs/install-sdk#linux). For x86_64 Linux, this user-local installation does not require `sudo`:

```bash
cd /tmp
curl -fLO https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz
tar -xzf google-cloud-cli-linux-x86_64.tar.gz -C "$HOME/.local"
"$HOME/.local/google-cloud-sdk/install.sh"
```

Allow the installer to update `PATH`, then open a new terminal. For ARM64 Linux, use the `google-cloud-cli-linux-arm.tar.gz` archive listed by Google instead.

Confirm the installation on any platform:

```bash
gcloud version
```

## Configure the project and authentication

Replace `YOUR_PROJECT_ID` in these commands. Run them once on each development machine:

```bash
gcloud init
gcloud config set project YOUR_PROJECT_ID
gcloud services enable bigquery.googleapis.com
gcloud auth application-default login --scopes=https://www.googleapis.com/auth/cloud-platform
gcloud auth application-default set-quota-project YOUR_PROJECT_ID
```

`gcloud init` authenticates the CLI. `gcloud auth application-default login` is a separate login that creates credentials for Python client libraries. Both are needed here.

On Google's ADC consent page, allow the requested Google Cloud access. The OAuth scope sounds broad, but IAM still restricts the account to its assigned permissions.

For a remote Linux host, WSL session, or SSH session that cannot open a browser, use:

```bash
gcloud init --console-only
gcloud auth application-default login --no-launch-browser --scopes=https://www.googleapis.com/auth/cloud-platform
gcloud auth application-default set-quota-project YOUR_PROJECT_ID
```

Open the displayed URL on a trusted browser and enter the one-time code directly in the terminal. Do not send that code through chat, email, or an issue.

## Install the notebook environment

From the repository root:

```bash
uv sync --extra stats
```

In VS Code, select this repository's `.venv` as the Jupyter kernel:

- Linux/macOS: `.venv/bin/python`
- Windows: `.venv\Scripts\python.exe`

In a multi-root workspace, check the full path carefully so the sibling `micropython-stubber` environment is not selected.

## Verify the complete setup

From the repository root, run this harmless query:

```bash
uv run --extra stats python -c "import google.auth; from google.cloud import bigquery; credentials, detected = google.auth.default(); project = detected or credentials.quota_project_id; row = next(iter(bigquery.Client(project=project, credentials=credentials).query('SELECT 1 AS value').result())); print(f'project={project}, result={row.value}')"
```

A working setup prints the selected project and `result=1` without printing any token or secret.

Then open `statistics/1-update_stats.ipynb`, select the correct kernel, and run the cells from the top. The updater queries only completed months and writes the merged results to `downloads.csv`. Run `statistics/2-report-stats.ipynb` afterward to refresh the charts.

## Credential security

ADC user credentials contain a refresh token and are stored outside this repository:

- Linux/macOS: `~/.config/gcloud/application_default_credentials.json`
- Windows: `%APPDATA%\gcloud\application_default_credentials.json`

Do not copy this file between machines or commit it. Authenticate separately on each machine. Revoke local ADC when a machine is retired or no longer trusted:

```bash
gcloud auth application-default revoke
```

This does not remove the normal `gcloud` CLI login. Use `gcloud auth revoke` separately if that login must also be removed.

## Troubleshooting

### `cloud-platform scope is required but not consented`

Repeat the ADC command with the explicit scope and allow the Google Cloud permission on the consent page:

```bash
gcloud auth application-default login --scopes=https://www.googleapis.com/auth/cloud-platform
```

### `DefaultCredentialsError: Your default credentials were not found`

Run the ADC login command, restart the Jupyter kernel, and rerun the notebook from the top. Also remove `GOOGLE_APPLICATION_CREDENTIALS` from the environment if it points to an old JSON key.

### `403` or missing `bigquery.jobs.create`

Grant the signed-in user **BigQuery Job User** (`roles/bigquery.jobUser`) on the query project.

### Quota-project or `serviceusage.services.use` error

Confirm the project and reset the ADC quota project:

```bash
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default set-quota-project YOUR_PROJECT_ID
```

If it is not your project, ask its administrator for `serviceusage.services.use`.

### BigQuery API is disabled

```bash
gcloud services enable bigquery.googleapis.com --project=YOUR_PROJECT_ID
```

### `google.auth` or `google.cloud.bigquery` cannot be imported

Run `uv sync --extra stats`, restart VS Code or the notebook kernel, and select this repository's `.venv` rather than a global or sibling-project interpreter.

## References

- [Authenticate to BigQuery](https://cloud.google.com/bigquery/docs/authentication)
- [Set up ADC for local development](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment)
- [Install the Google Cloud CLI](https://cloud.google.com/sdk/docs/install-sdk)
- [BigQuery IAM roles](https://cloud.google.com/bigquery/docs/access-control)
