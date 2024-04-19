 #!/bin/bash
 curl --head -s $1 | grep Location | cut -d' ' -f2