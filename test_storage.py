import tempfile

from pgbackup import storage

def test_storing_file_locally():
    infile = tempfile.TemporaryFile('r+b')
    infile.write(b"Testing")
    infile.seek(0)

    outfile = tempfile.NamedTemporaryFile(delete=False)
    storage.local(infile, outfile)
    with open(outfile.name, 'rb') as f:
        assert f.read() == b"Testing"

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()