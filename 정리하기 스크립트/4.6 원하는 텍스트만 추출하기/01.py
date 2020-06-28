import re

text = '#1##23##456#'

pattern0 = re.compile(r'#\w{2}#')        # '#\w\w#' 탐색
pattern1 = re.compile(r'#\w{2,3}#')      # '#\w\w#' 혹은 r'#\w\w\w#' 탐색
pattern2 = re.compile(r'#\w?#')          # '#\w#' 혹은 '##' 탐색
pattern3 = re.compile(r'#\w+#')          # '#\w ...#' 탐색

print(re.findall(pattern0, text))
print(re.findall(pattern1, text))
print(re.findall(pattern2, text))
print(re.findall(pattern3, text))
