# GDrive2Direct

Script to get direct download links from **publicly** viewable Google Drive file url

## Usage

### Minimal

`$ python2 gdrive2direct.py link1 link2 link3 ...`

### Specify a label for each url

Pass links in the form label::url

`$ python2 gdrive2direct.py label1::url1 label2::url2 label3::url3 ...`

### Save output to file

Use `-o` flag with a filename.json to get output in a json file

`$ python2 gdrive2direct.py -o output_file.json link1 link2 link3 ...`

output_file.json will have keys corresponding to labels if specified else default numbered keys will be used

### Example usage
`$ python2 gdrive2direct.py -o test.json ai-seminar::https://drive.google.com/file/d/1hDOR0PwbyrlGXtVLe6LrruW21BRpgvc-/view?usp=sharing ar-workshop::https://drive.google.com/file/d/1rMiqSQp6w4Jh1qkgXquV179mQlgqwr6Z/view?usp=sharing code-break::https://drive.google.com/file/d/17JpuItSv7Cf2l34hzJQ5_gWO-yKobQ4M/view?usp=sharing`

Output file:
```json
{
    "ar-workshop": "https://drive.google.com/uc?export=download&id=1rMiqSQp6w4Jh1qkgXquV179mQlgqwr6Z", 
    "ai-seminar": "https://drive.google.com/uc?export=download&id=1hDOR0PwbyrlGXtVLe6LrruW21BRpgvc-", 
    "code-break": "https://drive.google.com/uc?export=download&id=17JpuItSv7Cf2l34hzJQ5_gWO-yKobQ4M"
}
```


Note: A publicly viewable google drive file url usually looks like this:

https://drive.google.com/file/d/random_string/view?usp=sharing

