import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.col_pins = (board.GP0,)
keyboard.row_pins = (board.GP1,)

_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.keymap = [ [ KC.A, ], ]

# keyboard.keymap = [
    # Keymap _LBL: Linux Base Layer (Default Layer)
    # ┌───┐   ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┐
    # │Esc│   │M1 │M3 │M2 │M4 │ │M1 │M3 │M2 │M4 │ │M1 │M3 │M2 │M4 │ │PSc│Slk│Pse│
    # └───┘   └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┘
    # ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐ ┌───┬───┬───┐
    # │ ` │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 0 │ - │ = │ Backsp│ │Ins│Hom│PgU│
    # ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ ├───┼───┼───┤
    # │ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │ [ │ ] │  \  │ │Del│End│PgD│
    # ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬────┤ └───┴───┴───┘
    # │ Ctrl │ A │ S │ D │ F │ G │ H │ J │ K │ L │ ; │ ' │ # │Entr│
    # ├────┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴────┤     ┌───┐
    # │Shft│ \ │ Z │ X │ C │ V │ B │ N │ M │ , │ . │ / │    Shift │     │ ↑ │
    # ├────┼───┴┬──┴─┬─┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ ┌───┼───┼───┐
    # │Func│GUI │Alt │                        │ Alt│Func│ App│Ctrl│ │ ← │ ↓ │ → │
    # └────┴────┴────┴────────────────────────┴────┴────┴────┴────┘ └───┴───┴───┘
#     [
#         KC.ESC,           KC.BTN1, KC.BTN3, KC.BTN2, KC.BTN4, KC.BTN1, KC.BTN3, KC.BTN2, KC.BTN4, KC.BTN1, KC.BTN3, KC.BTN2, KC.BTN4,    KC.PSCR, KC.SLCK, KC.PAUS,
#         KC.GRV,  KC.1,    KC.2,    KC.3,    KC.4,    KC.5,    KC.6,    KC.7,    KC.8,    KC.9,    KC.0,    KC.MINS, KC.EQL,  KC.BSPC,    KC.INS,  KC.HOME, KC.PGUP,
#         KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,    KC.DEL,  KC.END,  KC.PGDN,
#         KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.NUHS, KC.ENT,
#         KC.LSFT, KC.NUBS, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,          KC.RSFT,             KC.UP,
#         KC.WFN,  KC.LGUI, KC.LALT,                            KC.SPC,                             KC.RALT, KC.WFN,  KC.APP,  KC.RCTL,    KC.LEFT, KC.DOWN, KC.RGHT,
#     ],
    # Keymap _LFL: Linux Function Layer
    # ┌───┐   ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┐
    # │   │   │F1 │F2 │F3 │F4 │ │F5 │F6 │F7 │F8 │ │F9 │F10│F11│F12│ │   │   │Mut│
    # └───┘   └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┘
    # ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐ ┌───┬───┬───┐
    # │   │   │   │   │   │   │   │   │   │   │   │   │   │       │ │   │   │Vo+│
    # ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ ├───┼───┼───┤
    # │     │   │   │   │   │   │   │   │   │   │   │   │   │     │ │   │   │Vo-│
    # ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬────┤ └───┴───┴───┘
    # │ Caps │   │   │   │   │   │   │   │   │   │   │   │   │    │
    # ├────┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴────┤     ┌───┐
    # │    │   │   │   │   │   │   │   │   │   │   │   │          │     │   │
    # ├────┼───┴┬──┴─┬─┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ ┌───┼───┼───┐
    # │    │Lock│    │                        │    │Func│ Sys│    │ │   │   │   │
    # └────┴────┴────┴────────────────────────┴────┴────┴────┴────┘ └───┴───┴───┘
#     [
#         _______,          KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,     _______, _______, KC.MUTE,
#         _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,    _______, _______, KC.VOLU,
#         _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,    _______, _______, KC.VOLD,
#         KC.CAPS, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
#         _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,          _______,             _______,
#         _______, KC.TGUI, _______,                            _______,                            _______, _______, MO_LSL,  _______,    _______, _______, _______,
#     ],
    # Keymap _LSL: Linux System Layer
    # ┌───┐   ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┐
    # │Rst│   │Slp│   │   │Pwr│ │   │   │   │   │ │   │   │   │MAC│ │   │   │   │
    # └───┘   └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┘
    # ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐ ┌───┬───┬───┐
    # │   │   │   │   │   │   │   │   │   │   │   │   │   │       │ │   │   │   │
    # ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ ├───┼───┼───┤
    # │     │   │   │   │   │   │   │   │   │   │   │   │   │     │ │   │   │   │
    # ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬────┤ └───┴───┴───┘
    # │      │   │   │DBG│   │   │   │   │   │   │   │   │   │    │
    # ├────┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴────┤     ┌───┐
    # │    │   │   │   │   │   │   │   │   │   │   │   │          │     │   │
    # ├────┼───┴┬──┴─┬─┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ ┌───┼───┼───┐
    # │    │    │    │                        │    │    │    │    │ │   │   │   │
    # └────┴────┴────┴────────────────────────┴────┴────┴────┴────┘ └───┴───┴───┘
#     [
#         QK_BOOT,          KC.SLEP, XXXXXXX, XXXXXXX, KC.PWR,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, DF_W2MBL,   XXXXXXX, XXXXXXX, XXXXXXX,
#         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX,
#         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX,
#         XXXXXXX, XXXXXXX, XXXXXXX, DEBUG,   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
#         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,          XXXXXXX,             XXXXXXX,
#         XXXXXXX, XXXXXXX, XXXXXXX,                            XXXXXXX,                            XXXXXXX, _______, _______, XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX,
#     ],
    # Keymap _MBL: macOS Base Layer (Alternate Layout)
    # ┌───┐   ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┐
    # │Esc│   │M1 │M3 │M2 │M4 │ │M1 │M3 │M2 │M4 │ │M1 │M3 │M2 │M4 │ │F13│F14│F15│
    # └───┘   └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┘
    # ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐ ┌───┬───┬───┐
    # │ ` │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 0 │ - │ = │ Backsp│ │Ins│Hom│PgU│
    # ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ ├───┼───┼───┤
    # │ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │ [ │ ] │  \  │ │Del│End│PgD│
    # ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬────┤ └───┴───┴───┘
    # │ Ctrl │ A │ S │ D │ F │ G │ H │ J │ K │ L │ ; │ ' │ # │Entr│
    # ├────┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴────┤     ┌───┐
    # │Shft│ \ │ Z │ X │ C │ V │ B │ N │ M │ , │ . │ / │    Shift │     │ ↑ │
    # ├────┼───┴┬──┴─┬─┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ ┌───┼───┼───┐
    # │Func│Alt │GUI │                        │ GUI│ Alt│Func│Ctrl│ │ ← │ ↓ │ → │
    # └────┴────┴────┴────────────────────────┴────┴────┴────┴────┘ └───┴───┴───┘
#     [
#         KC.ESC,           KC.BTN1, KC.BTN3, KC.BTN2, KC.BTN4, KC.BTN1, KC.BTN3, KC.BTN2, KC.BTN4, KC.BTN1, KC.BTN3, KC.BTN2, KC.BTN4,    KC.F13,  KC.F14,  KC.F15,
#         KC.GRV,  KC.1,    KC.2,    KC.3,    KC.4,    KC.5,    KC.6,    KC.7,    KC.8,    KC.9,    KC.0,    KC.MINS, KC.EQL,  KC.BSPC,    KC.INS,  KC.HOME, KC.PGUP,
#         KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,    KC.DEL,  KC.END,  KC.PGDN,
#         KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.NUHS, KC.ENT,
#         KC.LSFT, KC.NUBS, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,          KC.RSFT,             KC.UP,
#         KC.MFN,  KC.LALT, KC.LGUI,                            KC.SPC,                             KC.RGUI, KC.RALT, KC.MFN,  KC.RCTL,    KC.LEFT, KC.DOWN, KC.RGHT,
#     ],
    # Keymap _MFL: macOS Function Layer
    # ┌───┐   ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┐
    # │   │   │F1 │F2 │F3 │F4 │ │F5 │F6 │F7 │F8 │ │F9 │F10│F11│F12│ │TMd│   │Mut│
    # └───┘   └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┘
    # ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐ ┌───┬───┬───┐
    # │   │   │   │   │   │   │   │   │   │   │   │   │   │       │ │   │   │Vo+│
    # ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ ├───┼───┼───┤
    # │     │   │   │   │   │   │   │   │   │   │   │   │   │     │ │   │   │Vo-│
    # ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬────┤ └───┴───┴───┘
    # │ Caps │   │   │   │   │   │   │   │   │   │   │   │   │    │
    # ├────┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴────┤     ┌───┐
    # │    │   │   │   │   │   │   │   │   │   │   │   │          │     │   │
    # ├────┼───┴┬──┴─┬─┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ ┌───┼───┼───┐
    # │    │    │    │                        │    │ Sys│Func│    │ │   │   │   │
    # └────┴────┴────┴────────────────────────┴────┴────┴────┴────┘ └───┴───┴───┘
#     [
#         _______,          KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,     KC.TMED, _______, KC.MUTE,
#         _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,    _______, _______, KC.VOLU,
#         _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,    _______, _______, KC.VOLD,
#         KC.CAPS, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
#         _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,          _______,             _______,
#         _______, _______, _______,                            _______,                            _______, MO_MSL,  _______, _______,    _______, _______, _______,
#     ],
    # Keymap _MSL: macOS System Layer
    # ┌───┐   ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┐
    # │Rst│   │   │   │   │Slp│ │   │   │   │   │ │   │   │   │LNX│ │   │   │   │
    # └───┘   └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┘
    # ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐ ┌───┬───┬───┐
    # │   │   │   │   │   │   │   │   │   │   │   │   │   │       │ │   │   │   │
    # ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ ├───┼───┼───┤
    # │     │   │   │   │   │   │   │   │   │   │   │   │   │     │ │   │   │   │
    # ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬────┤ └───┴───┴───┘
    # │      │   │   │DBG│   │   │   │   │   │   │   │   │   │    │
    # ├────┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴────┤     ┌───┐
    # │    │   │   │   │   │   │   │   │   │   │   │   │          │     │   │
    # ├────┼───┴┬──┴─┬─┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ ┌───┼───┼───┐
    # │    │    │    │                        │    │ Sys│Func│    │ │   │   │   │
    # └────┴────┴────┴────────────────────────┴────┴────┴────┴────┘ └───┴───┴───┘
#     [
#         QK_BOOT,          XXXXXXX, XXXXXXX, XXXXXXX, KC.SLEP, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, DF_M2LBL,   XXXXXXX, XXXXXXX, XXXXXXX,
#         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX,
#         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX,
#         XXXXXXX, XXXXXXX, XXXXXXX, DEBUG,   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
#         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,          XXXXXXX,             XXXXXXX,
#         XXXXXXX, XXXXXXX, XXXXXXX,                            XXXXXXX,                            XXXXXXX, _______, _______, XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX,
#     ],
# ]

if __name__ == '__main__':
    keyboard.go()
