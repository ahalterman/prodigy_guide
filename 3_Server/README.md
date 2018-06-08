# Running Prodigy on a Remote Server

Running Prodigy on a remote server is similar to running it locally. The main
differences consist of having Prodigy listen for requests coming from outside
the server, opening the needed ports on the server, and configuring basic
authentication to discourage unauthorized access.

### Changing network binding

Prodigy's configuration is set by a `.prodigy.json` file, either in Prodigy's
home directory (`~/.prodigy/`) or on a per-project basis in the directory where
Prodigy is started (the leading `.` is optional). By default, Prodigy only accepts requests coming from
`localhost` to prevent outside access. To have Prodigy accept requests from
outside, the Prodigy config needs to have `"host": "localhost"` changed to
`"host": 0.0.0.0"` (see included `.prodigy.json`).:w

### Opening ports on EC2

(screenshot here)

### Basic authentication

