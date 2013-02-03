{
  'targets': [
    {
      'target_name': 'liblibxl_bindings',
      'sources': [
        'src/libxl_bindings.cc',
        'src/libxl_book.cc'
      ],
      'conditions': [
        ['OS=="linux"', {
          'include_dirs': [
            'deps/libxl/include_cpp'
          ],
          'libraries': [
            '-lxl'
          ]
        }, {
          # only Linux is supported now ...
        }]
      ]
    }
  ]
}