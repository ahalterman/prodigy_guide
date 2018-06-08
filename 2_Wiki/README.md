# Wikipedia Example

This example shows how to take in a Wikipedia category page, generate
Prodigy-formatted JSONL to display them as iframes, and run a simple
classification display on them.

### Formatting tasks 

Prodigy expects tasks to come in a certain format. Here, where we're displaying
an external website as an iframe, we need to format it as a JSONL file (newline
delimited JSON) with an `html` frame containing valid HTML with an iframe.

`wiki_to_task.py` is example code to do this task:

```
python wiki_to_task.py -i https://en.wikipedia.org/wiki/Category:Towns_in_Oklahoma -o wiki_tasks.jsonl
```

where the link following `-i` is the Wikipedia category page to scrape, and the
file following `-o` is the file to write it out to.

### Running Prodigy

Once our Wikipedia links are formatted in the correct JSONL format, we can
start a Prodigy labeling session:

```
prodigy mark ucsd_wiki wiki_tasks.jsonl --label "SUBURBAN"
```

where

- `mark`: the Prodigy recipe to use (here, the no model-in-the-loop
classification model)
- `ucsd_wiki`: the name of the Prodigy dataset to store the annotations in
    (will be created automatically if this command is being run for the first
    time)
- `wiki_tasks.jsonl`: the file of tasks to annotate that we created above
- `--label "SUBURBAN"`: the label to use in annotating the examples


