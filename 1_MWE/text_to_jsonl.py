import jsonlines
import plac

@plac.annotations(
    text_file=("Location of newline-delimited text file to convert", "option", "i", str),
    output_file=("New file to write output JSONL to", "option", "o", str))
def main(text_file, output_file):
    # read in text
    with open(text_file, "r") as f:
        text = f.readlines()
    # convert to a list of dicts, with "text" as a key
    text = [{"text" : i.strip()} for i in text]
    # write out as newline-delim JSON for Prodigy
    with jsonlines.open(output_file, mode='w') as writer:
        writer.write_all(text)

if __name__ == '__main__':
    plac.call(main)
