# Copyright (c) 2011 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'ui_base',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '../build/temp_gyp/googleurl.gyp:googleurl',
        '../net/net.gyp:net',
        '../skia/skia.gyp:skia',
        '../third_party/icu/icu.gyp:icui18n',
        '../third_party/icu/icu.gyp:icuuc',
        'base/strings/ui_strings.gyp:ui_strings',
        'ui_gfx',
      ],
      # Export these dependencies since text_elider.h includes ICU headers.
      'export_dependent_settings': [
        '../third_party/icu/icu.gyp:icui18n',
        '../third_party/icu/icu.gyp:icuuc',
      ],
      'sources': [
        'base/accessibility/accessibility_types.h',
        'base/accessibility/accessible_view_state.cc',
        'base/accessibility/accessible_view_state.h',
        'base/animation/animation.cc',
        'base/animation/animation.h',
        'base/animation/animation_container.cc',
        'base/animation/animation_container.h',
        'base/animation/animation_container_element.h',
        'base/animation/animation_container_observer.h',
        'base/animation/animation_delegate.h',
        'base/animation/linear_animation.cc',
        'base/animation/linear_animation.h',
        'base/animation/multi_animation.cc',
        'base/animation/multi_animation.h',
        'base/animation/slide_animation.cc',
        'base/animation/slide_animation.h',
        'base/animation/throb_animation.cc',
        'base/animation/throb_animation.h',
        'base/animation/tween.cc',
        'base/animation/tween.h',
        'base/clipboard/clipboard.cc',
        'base/clipboard/clipboard.h',
        'base/clipboard/clipboard_linux.cc',
        'base/clipboard/clipboard_mac.mm',
        'base/clipboard/clipboard_util_win.cc',
        'base/clipboard/clipboard_util_win.h',
        'base/clipboard/clipboard_win.cc',
        'base/clipboard/scoped_clipboard_writer.cc',
        'base/clipboard/scoped_clipboard_writer.h',
        'base/dragdrop/drag_drop_types_gtk.cc',
        'base/dragdrop/drag_drop_types.h',
        'base/dragdrop/drag_drop_types_win.cc',
        'base/dragdrop/drag_source.cc',
        'base/dragdrop/drag_source.h',
        'base/dragdrop/drop_target.cc',
        'base/dragdrop/drop_target.h',
        'base/dragdrop/gtk_dnd_util.cc',
        'base/dragdrop/gtk_dnd_util.h',
        'base/dragdrop/os_exchange_data.cc',
        'base/dragdrop/os_exchange_data.h',
        'base/dragdrop/os_exchange_data_provider_gtk.cc',
        'base/dragdrop/os_exchange_data_provider_gtk.h',
        'base/dragdrop/os_exchange_data_provider_win.cc',
        'base/dragdrop/os_exchange_data_provider_win.h',
        'base/events.h',
        'base/gtk/event_synthesis_gtk.cc',
        'base/gtk/event_synthesis_gtk.h',
        'base/gtk/g_object_destructor_filo.cc',
        'base/gtk/g_object_destructor_filo.h',
        'base/gtk/gtk_im_context_util.cc',
        'base/gtk/gtk_im_context_util.h',
        'base/gtk/gtk_signal.h',
        'base/gtk/gtk_signal_registrar.cc',
        'base/gtk/gtk_signal_registrar.h',
        'base/gtk/gtk_windowing.cc',
        'base/gtk/gtk_windowing.h',
        'base/ime/composition_text.cc',
        'base/ime/composition_text.h',
        'base/ime/composition_underline.h',
        'base/ime/text_input_type.h',
        'base/keycodes/keyboard_code_conversion_gtk.cc',
        'base/keycodes/keyboard_code_conversion_gtk.h',
        'base/keycodes/keyboard_code_conversion_mac.h',
        'base/keycodes/keyboard_code_conversion_mac.mm',
        'base/keycodes/keyboard_code_conversion_win.cc',
        'base/keycodes/keyboard_code_conversion_win.h',
        'base/keycodes/keyboard_code_conversion_x.cc',
        'base/keycodes/keyboard_code_conversion_x.h',
        'base/keycodes/keyboard_codes.h',
        'base/l10n/l10n_font_util.cc',
        'base/l10n/l10n_font_util.h',
        'base/l10n/l10n_util.cc',
        'base/l10n/l10n_util.h',
        'base/l10n/l10n_util_collator.h',
        'base/l10n/l10n_util_mac.h',
        'base/l10n/l10n_util_mac.mm',
        'base/l10n/l10n_util_posix.cc',
        'base/l10n/l10n_util_win.cc',
        'base/l10n/l10n_util_win.h',
        'base/message_box_flags.h',
        'base/message_box_win.cc',
        'base/message_box_win.h',
        'base/models/accelerator_cocoa.h',
        'base/models/accelerator_cocoa.mm',
        'base/models/accelerator_gtk.h',
        'base/models/accelerator.h',
        'base/models/button_menu_item_model.cc',
        'base/models/button_menu_item_model.h',
        'base/models/combobox_model.h',
        'base/models/menu_model.cc',
        'base/models/menu_model.h',
        'base/models/menu_model_delegate.h',
        'base/models/simple_menu_model.cc',
        'base/models/simple_menu_model.h',
        'base/models/table_model.cc',
        'base/models/table_model.h',
        'base/models/table_model_observer.h',
        'base/models/tree_model.cc',
        'base/models/tree_model.h',
        'base/models/tree_node_iterator.h',
        'base/models/tree_node_model.h',
        'base/range/range.cc',
        'base/range/range.h',
        'base/range/range.mm',
        'base/resource/data_pack.cc',
        'base/resource/data_pack.h',
        'base/resource/resource_bundle.cc',
        'base/resource/resource_bundle.h',
        'base/resource/resource_bundle_linux.cc',
        'base/resource/resource_bundle_mac.mm',
        'base/resource/resource_bundle_posix.cc',
        'base/resource/resource_bundle_win.cc',
        'base/text/bytes_formatting.cc',
        'base/text/bytes_formatting.h',
        'base/text/text_elider.cc',
        'base/text/text_elider.h',
        'base/theme_provider.cc',
        'base/theme_provider.h',
        'base/ui_base_paths.cc',
        'base/ui_base_paths.h',
        'base/ui_base_switches.cc',
        'base/ui_base_switches.h',
        'base/view_prop.cc',
        'base/view_prop.h',
        'base/win/hwnd_util.cc',
        'base/win/hwnd_util.h',
        'base/win/ime_input.cc',
        'base/win/ime_input.h',
	'base/win/shell.cc',
	'base/win/shell.h',
        'base/win/window_impl.cc',
        'base/win/window_impl.h',
        'base/x/active_window_watcher_x.cc',
        'base/x/active_window_watcher_x.h',
        'base/x/x11_util.cc',
        'base/x/x11_util.h',
        'base/x/x11_util_internal.h',
      ],
      'conditions': [
        ['toolkit_uses_gtk == 1', {
          'dependencies': [
            '../build/linux/system.gyp:fontconfig',
            '../build/linux/system.gyp:gtk',
            '../build/linux/system.gyp:x11',
            '../build/linux/system.gyp:xext',
          ],
          'link_settings': {
            'libraries': [
              '-lXrender',  # For XRender* function calls in x11_util.cc.
            ],
          },
          'conditions': [
            ['toolkit_views==0', {
              # Note: because of gyp predence rules this has to be defined as
              # 'sources/' rather than 'sources!'.
              'sources/': [
                ['exclude', '^base/dragdrop/drag_drop_types_gtk.cc'],
                ['exclude', '^base/dragdrop/os_exchange_data.cc'],
                ['exclude', '^base/dragdrop/os_exchange_data.h'],
                ['exclude', '^base/dragdrop/os_exchange_data_provider_gtk.cc'],
                ['exclude', '^base/dragdrop/os_exchange_data_provider_gtk.h'],
              ],
            }, {
              # Note: because of gyp predence rules this has to be defined as
              # 'sources/' rather than 'sources!'.
              'sources/': [
                ['include', '^base/dragdrop/os_exchange_data.cc'],
              ],
            }],
          ],
        }],
        ['OS!="win"', {
          'sources!': [
            'base/dragdrop/drag_source.cc',
            'base/dragdrop/drag_source.h',
            'base/dragdrop/drag_drop_types.h',
            'base/dragdrop/drop_target.cc',
            'base/dragdrop/drop_target.h',
            'base/dragdrop/os_exchange_data.cc',
            'base/view_prop.cc',
            'base/view_prop.h',
          ],
          'sources/': [
            ['exclude', '^base/win/*'],
          ],
        }],
        ['OS=="mac"', {
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/Accelerate.framework',
              '$(SDKROOT)/System/Library/Frameworks/AudioUnit.framework',
            ],
          },
        }],
        ['use_x11==1', {
          'all_dependent_settings': {
            'ldflags': [
              '-L<(PRODUCT_DIR)',
            ],
            'link_settings': {
              'libraries': [
                '-lX11',
                '-ldl',
              ],
            },
          },
        }, {  # use_x11==0
          'sources!': [
            'base/keycodes/keyboard_code_conversion_x.cc',
            'base/keycodes/keyboard_code_conversion_x.h',
          ],
        }],
      ],
    },
  ],
  'conditions': [
    ['OS=="win"', {
      'targets': [
        {
          'target_name': 'ui_base_nacl_win64',
          'type': 'static_library',
          'defines': [
            '<@(nacl_win64_defines)',
          ],
          'sources': [
            'base/resource/resource_bundle_dummy.cc',
            'base/ui_base_paths.h',
            'base/ui_base_paths.cc',
            'base/ui_base_switches.h',
            'base/ui_base_switches.cc',
          ],
          'include_dirs': [
            '..',
          ],
          'configurations': {
            'Common_Base': {
              'msvs_target_platform': 'x64',
            },
          },
        },
      ],
    }],
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
