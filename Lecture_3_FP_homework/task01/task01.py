# Using functional approach, generators, currying,
# implement functions that writes IP list of redirected requests (code 304) into another file
# separate pure_func from functions that change state (io_func)
# write negative test "test_myfunc_negative"
# Set pytest as default runner https://stackoverflow.com/questions/6397063/how-do-i-configure-pycharm-to-run-py-test-tests
# hit Ctrl+Shift+F10 or RMB on the file to run tests


def io_func(logfile_path, result_file_path):
    with open(logfile_path, mode="r") as file_input, \
         open(result_file_path, mode="w") as file_output:
        for line in file_input:
            ip = pure_func(line)
            if ip is not None:
                file_output.write(f"{ip}\n")


def pure_func(file_line):
    line_parts = file_line.split()
    return line_parts[0] if "304" in line_parts else None


def test_myfunc_positive():
    line = '218.30.103.62 - - [17/May/2015:11:05:17 +0000] "GET /projects/xdotool/xdotool.xhtml \
    HTTP/1.1" 304 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"'
    assert pure_func(line) == "218.30.103.62"


def test_myfunc_negative():
    line = '218.30.103.62 - - [17/May/2015:11:05:17 +0000] "GET /projects/xdotool/xdotool.xhtml \
    HTTP/1.1" 200 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"'
    assert pure_func(line) is None
