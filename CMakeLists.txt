cmake_minimum_required(VERSION 3.19)
project(Elise LANGUAGES CXX)

find_package(Qt6 6.5 REQUIRED COMPONENTS Core Widgets)

set(CMAKE_AUTORCC ON)

qt_standard_project_setup()

qt_add_executable(Elise
    WIN32 MACOSX_BUNDLE
    elise.qrc
    main.cpp
    mainwindow.cpp
    mainwindow.h
    regexp_highlighter.cpp
    regexp_highlighter.h
    mainwindow.ui
)

target_link_libraries(Elise
    PRIVATE
        Qt::Core
        Qt::Widgets
)


include(GNUInstallDirs)

install(TARGETS Elise
    BUNDLE  DESTINATION .
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

qt_generate_deploy_app_script(
    TARGET Elise
    OUTPUT_SCRIPT deploy_script
    NO_UNSUPPORTED_PLATFORM_ERROR
)

set_target_properties(Elise PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED ON
)

install(SCRIPT ${deploy_script})
