# IMDB Review Classification

## First Steps

- Please clone this repository to your local device:
`
git clone https://github.com/xstasyAI-alt/imdb-review-classification.git
`

- Download the IMDB Movie Review Dataset:
`
sh scripts/download_data.sh
`

- Install packages:
`
pip install -r requirements.txt
`

## Run Locally
```
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

- Go to https://localhost:8000/docs.

## Miscellaneous
- Before pushing code or create Merge Requests:
`
sh scripts/format.sh
`

## Git Commands
- Create new branch:
`
git checkout -b <branch_name>
`
  - `<branch_name>` should follow the conventions: `feature/some_feature`, `improve/some_improvement`, `fix/some_bug`, etc.
- Change branch: `git checkout <branch_name>`
- Add new code to branch: `git add -u`
- Commit: `git commit -m "<some_message>"`:
  - `<some_message>` can be anything but showing what you have done, what are the changes, etc. should be better
- Push to repository: `git push`

## Project Structure
```
|---data
|---scripts
|---src
|   |---app.py
|   |---common
|   |   |---prprocess_text.py
|   |   |---utils.py
```
