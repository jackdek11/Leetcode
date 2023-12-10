# Read from the file file.txt and print its transposed content to stdout.
#!/bin/bash
awk '{
    for (i = 1; i <= NF; i++) {
        if (NR == 1) {
            transposed[i] = $i;
        } else {
            transposed[i] = transposed[i] " " $i;
        }
    }
}
END {
    for (i = 1; i <= NF; i++) {
        print transposed[i];
    }
}' file.txt