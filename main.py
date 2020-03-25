import csv
import io


def main():
    # my_input = os.environ["INPUT_MYINPUT"]
    my_input = "Jorge"

    outBuffer = io.StringIO()
    with open('sampleFiles/a.csv', 'r') as csvfile:
        reader = csv.reader(
            csvfile, quoting=csv.QUOTE_NONNUMERIC, skipinitialspace=True)
        writer = csv.writer(
            outBuffer, quoting=csv.QUOTE_NONNUMERIC, skipinitialspace=True)
        for row in reader:
            writer.writerow(row)

    # Add new lines
    writer.writerow([my_input, 'M', 25.0, 128.0, 205.0])
    output = outBuffer.getvalue().replace('\n', '%0A')
    print(f"::set-output name=myOutput::{output}")
    outBuffer.close()


if __name__ == "__main__":
    main()
