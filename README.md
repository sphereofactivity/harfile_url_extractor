# harfile_url_extractor
URL extractor for HAR Files when hardening connections through administrative permissions. 

## Requirements 
urlparse <br>
json

## Purpose
A tool to use to speed up determining URL connections to a website. Intended to speed up the process of manually searching through HAR files or the Developer console for connections, a security member can scroll through a page, collect all connections, save the HAR file,
the run the script and provide a path to the HAR File and it will extract the network location in URL format removing the path segment:

https://example.com/path-segment -> example.com

The tool will also not print any URL that already exists in the list to prevent repeated listing of URLs and allowing for an easier path to hardening active internet connections through administrative positions.

## Next Steps
To take this tool further - a list of already allowed URLs can be stored in a location, for example a CSV file. The tool can be configured on the end-user side to auth to wherever the file is stored or path if local, and compare the stored list of found URLs to the existing list and choose not to print into the terminal list,
therefore further reducing the toil of needing to start through which URLs are already allowed and which have yet to be allowed.
