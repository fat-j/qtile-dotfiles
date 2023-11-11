    
#       █████████     ███████    ███████████ █████ █████ ███████████ █████ █████       ██████████
#      ███░░░░░███  ███░░░░░███ ░█░░░░░░███ ░░███ ░░███ ░█░░░███░░░█░░███ ░░███       ░░███░░░░░█
#     ███     ░░░  ███     ░░███░     ███░   ░░███ ███  ░   ░███  ░  ░███  ░███        ░███  █ ░ 
#    ░███         ░███      ░███     ███      ░░█████       ░███     ░███  ░███        ░██████   
#    ░███         ░███      ░███    ███        ░░███        ░███     ░███  ░███        ░███░░█   
#    ░░███     ███░░███     ███   ████     █    ░███        ░███     ░███  ░███      █ ░███ ░   █
#     ░░█████████  ░░░███████░   ███████████    █████       █████    █████ ███████████ ██████████
#      ░░░░░░░░░     ░░░░░░░    ░░░░░░░░░░░    ░░░░░       ░░░░░    ░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░ 
#
#                                                                                    - DARKKAL44
  


from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from time import sleep

mod = "mod4"
terminal = "alacritty"

# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█




keys = [

    #  D E F A U L T

    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "control"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc='powermenu'),
    Key([mod], "t", lazy.spawn("sh -c ~/.config/rofi/scripts/themes"), desc='theme_switcher'),

    # # C U S T O M

    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
    Key([mod],"e", lazy.spawn("thunar Downloads"), desc='file manager'),
	Key([mod], "v", lazy.spawn("roficlip"), desc='clipboard'),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
	Key([mod], "g", lazy.spawn("goneovim"), desc='Text editor'),
	Key([mod], "w", lazy.spawn("brave"), desc='Web browser'),
    Key([mod], "d", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "c", lazy.spawn("rofi -show calc -modi calc -no-show-match -no-sort"), desc="Calculator in rofi"),
	Key([mod], "n", lazy.spawn("dunstctl history-pop"), desc='Notification history'),
]



# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█



groups = [Group(f"{i+1}", label="󰏃") for i in range(8)]

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )




# L A Y O U T S




layouts = [
    layout.Columns( margin= [1,2,1,2], border_focus='#FF0000',
	    border_normal='#1F1D2E',
        border_width=3,
    ),

    layout.Max(	border_focus='#FF0000',
	    border_normal='#1F1D2E',
	    margin=0,
	    border_width=0,
    ),

    layout.Floating(	border_focus='#FF0000',
	    border_normal='#1F1D2E',
	    margin=0,
	    border_width=0,
	),

    # Try more layouts by unleashing below layouts

    # layout.Stack(num_stacks=2),

     layout.Bsp( border_focus='#FF0000',
	    border_normal='#1F1D2E',
	    margin=1,
	    border_width=3,
	),

     layout.Tile( border_focus='#FF0000',
	    border_normal='#1F1D2E',
	    margin=1,
	    border_width=3,
	),
     
     layout.Matrix(	border_focus='#FF0000',
	    border_normal='#1F1D2E',
	    margin=1,
	    border_width=3,
	),

   # layout.MonadTall(	border_focus='#FF0000',
   #	border_normal='#1F1D2E',
   #    margin=1,
   #    border_width=3,
   #),

   # layout.MonadWide(	border_focus='#FF0000',
#	    border_normal='#1F1D2E',
#	    margin=1,
#	    border_width=3,
#	),

   # layout.RatioTile(),
   # layout.Tile(	border_focus='#FF0000',
#	    border_normal='#1F1D2E',
   #    border_width=3
   #),

     layout.TreeTab(),

   #  layout.VerticalTile(),

   #  layout.Zoomy(),
]



widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = [ widget_defaults.copy()
        ]



def search():
    qtile.cmd_spawn("rofi -show drun")

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")

# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄



screens = [

    Screen(
        bottom=bar.Bar(
            [
				widget.Spacer(length=15,
                    background='#282738',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1":power},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),


                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='block',
                    active='#CAA9E0',
                    block_highlight_text_color="#91B1F0",
                    highlight_color='#4B427E',
                    inactive='#282738',
                    foreground='#4B427E',
                    background='#353446',
                    this_current_screen_border='#353446',
                    this_screen_border='#353446',
                    other_current_screen_border='#353446',
                    other_screen_border='#353446',
                    urgent_border='#353446',
                    rounded=True,
                    disable_drag=True,
                 ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background="#353446"
                ),


                widget.CurrentLayout(
                    background='#353446',
                    foreground='#CAA9E0',
                    fmt='{}',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/search.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1": search},
                ),

                widget.TextBox(
                    fmt='Search',
                    background='#282738',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground='#CAA9E0',
                    mouse_callbacks={"Button1": search},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',
                ),


                widget.WindowName(
                    background = '#353446',
                    format = "{name}",
                    font='JetBrains Mono Bold',
                    foreground='#CAA9E0',
                    empty_group_string = 'Desktop',
                    fontsize=13,

                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/3.png',
                ),


                widget.Systray(
                    background='#282738',
                    fontsize=2,
                ),


                widget.TextBox(
                    text=' ',
                    background='#282738',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                    background='#353446',
                ),


                # widget.Image(
                # filename='~/.config/qtile/Assets/Drop1.png',
                # ),


                # widget.Net(
                # format=' {up}   {down} ',
                # background='#353446',
                # foreground='#CAA9E0',
                # font="JetBrains Mono Bold",
                # prefix='k',
                # ),

                # widget.Image(
                    # filename='~/.config/qtile/Assets/2.png',
                # ),

                # widget.Spacer(
                    # length=8,
                    # background='#353446',
                # ),


                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/ram.png',
                    background='#353446',
                ),


                widget.Spacer(
                    length=-7,
                    background='#353446',
                ),


                widget.Memory(
                    background='#353446',
                    format='{MemUsed: .0f}{mm}',
                    foreground='#CAA9E0',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                ),



                # widget.Image(
                # filename='~/.config/qtile/Assets/Drop2.png',
                # ),



                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),


                widget.BatteryIcon(
                    theme_path='~/.config/qtile/Assets/Battery/',
                    background='#353446',
                    scale=1,
                ),


                widget.Battery(
                    font='JetBrains Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    format='{percent:2.0%}',
                    fontsize=13,
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),


                # widget.Battery(format=' {percent:2.0%}',
                    # font="JetBrains Mono ExtraBold",
                    # fontsize=12,
                    # padding=10,
                    # background='#353446',
                # ),

                # widget.Memory(format='﬙{MemUsed: .0f}{mm}',
                    # font="JetBrains Mono Bold",
                    # fontsize=12,
                    # padding=10,
                    # background='#4B4D66',
                # ),

                widget.Volume(
                    font='JetBrainsMono Nerd Font',
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    fontsize=13,
                    background='#353446',
                ),


                widget.Spacer(
                    length=-5,
                    background='#353446',
                    ),


                widget.Volume(
                    font='JetBrains Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    fontsize=13,
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),
                 

                widget.Wlan(
                    background='#353446',
                    foreground='#CAA9E0',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                    format='{essid} {percent:2.0%}'
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background='#353446',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/clock.png',
                    background='#282738',
                    margin_y=6,
                    margin_x=5,
                ),


                widget.Clock(
                    format='%I:%M %p',
                    background='#282738',
                    foreground='#CAA9E0',
                    font="JetBrains Mono Bold",
                    fontsize=15,
                ),


                widget.Spacer(
                    length=18,
                    background='#282738',
                ),



            ],
            45,
            border_color = '#282738',
            border_width = [0,0,0,0],
            margin = [0,0,0,0],

        ),
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
	border_focus='#1F1D2E',
	border_normal='#1F1D2E',
	border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)




from libqtile import hook
# some other imports
import os
import subprocess
# stuff
@hook.subscribe.startup_once
def autostart_once():
    subprocess.run('/home/user/.config/qtile/autostart_once.sh')# path to my script, under my user directory
    subprocess.call([home])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.client_new
def client_new(client):
    if client.name == 'New Tab - Brave':
        client.togroup("2")
# E O F
