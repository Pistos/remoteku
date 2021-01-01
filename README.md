# remoteku

A web app that lets you control Roku devices on your local network

## Setup

### Backend

[As per the Python documentation](https://docs.python.org/3/tutorial/venv.html),
create a Python virtual environment:

    python3 -m venv venv

Enter the Python virtual environment:

    . venv/bin/activate

Install the dependencies:

    python -m pip install -r requirements.txt

### Frontend

Install the dependencies:

    cd frontend
    npm install

## Getting Started

Two daemons need to be running: the backend and the frontend.

Start the backend (from the root of the repository):

    ./start-server.sh

Start the frontend (in another shell/terminal):

    cd frontend
    npm run serve

Visit http://ip.of.serving.host:8080 in a browser.

[As per Vue CLI documentation](https://cli.vuejs.org/config/#devserver)
and [webpack documentation](https://webpack.js.org/configuration/dev-server/#devserverport),
a different frontend port than 8080 can be specified thus:

    npm run serve -- --port 8081

## Usage

Upon visiting the web app, the app scans the local network for Roku devices,
and lists them by IP address.  Choose one, and then a graphical representation
of a physical Roku remote control will be presented.  Below the remote control
is a text field used for quick text entry on the Roku.  Below that is a grid of
Roku apps that are installed on the chosen Roku.

For most buttons on the virtual remote, clicking/tapping on them will send the
button press to the Roku.  (At this time, not all button presses are
implemented.)  The keyboard of the browsing device can also be used; see
Keyboard Shortcuts section, below.

After a text field is activated on the Roku, the text field in the remoteku web
app can be used to quickly send keystrokes to the Roku (in a batch) to fill in
the text field on the Roku.

### Keyboard Shortcuts

| Key | Button pressed |
|---|---|
| Up arrow | Up |
| Down arrow | Down |
| Left arrow | Left |
| Right arrow | Right |
| Enter | OK |
| Backspace | Back |
| Esc | Back |
| Space | Play/Pause |
| Page Up | Rewind |
| Page Down | Fast Forward |
