import os
import subprocess32 as subprocess

def crawl_site(base_url, RECURSE_DEPTH=1, CRAWL_DIRECTORY='/tmp/crawled-sites/', REJECT_EXTENSIONS=''):
  """
  Function wrapping wget to crawl a website.
  
  REJECT_EXTENSIONS should be given as a comma-separated list of extensions as a string:
    for example 'jpg,png,gif,mp3,mp4,pdf'.
    
  Returns the exit code of the wget subprocess.
  """
  
  # Build the wget command.
  args = [
    'wget',
    '--recursive',
    '--timestamping',
    '--level=%s' %RECURSE_DEPTH,
    '--directory-prefix=%s' %CRAWL_DIRECTORY,
    '--limit-rate=100k',
    '--wait=2',
    '--random-wait',
    '--ignore-length',  # Don't trust server-reported content length.
    '--no-parent',  # Only recurse paths below the given url.
    '--reject=%s' %REJECT_EXTENSIONS,
    '--save-headers',  # Use to restrict content types and other filters.
    '--adjust-extension',
    '--no-verbose',
    base_url
  ]
  
  # Run the recursive fetch.
  try:
    crawler = subprocess.check_output(args)
  except subprocess.CalledProcessError as e:
    print e.output
    return e.returncode
  else:
    return 0
