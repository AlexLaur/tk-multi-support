# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import tempfile

import sgtk

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtGui, QtCore
from .ui.dialog import Ui_Dialog
from .collector import DataCollector

# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)


def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system.

    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog(
        "Contact Studio Support", app_instance, AppDialog
    )


class AppDialog(QtGui.QWidget, Ui_Dialog):
    """
    Main application dialog window
    """

    def __init__(self):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        super(AppDialog, self).__init__()

        # now load in the UI that was created in the UI designer
        self.setupUi(self)
        self.pub_send.setEnabled(False)

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        self._app = sgtk.platform.current_bundle()

        # logging happens via a standard toolkit logger
        logger.info("Launching Support Application")

        # Data collector
        self._data_collector = DataCollector()
        self._report = self._data_collector.collect()

        # Signals
        self.lie_subject.textChanged.connect(self.on_text_edited)
        self.txe_content.textChanged.connect(self.on_text_edited)
        self.pub_send.clicked.connect(self.on_send_report_requested)
        self.item_thumbnail.screen_grabbed.connect(self.on_thumbnail_created)

    @QtCore.Slot()
    def on_send_report_requested(self):
        """Called when the Report need to be send."""
        logger.info("The report will be sent...")
        self._report.subject = self.lie_subject.text()
        self._report.content = self.txe_content.toPlainText()

        self._app.execute_hook_method(
            "hook_send_report", "send", report=self._report
        )

        self.close()
        logger.info("Closing the app.")

    @QtCore.Slot(object)
    def on_thumbnail_created(self, pixmap):
        """Called when a thumbnail has been created.

        :param pixmap: The thumbnail
        :type pixmap: QPixmap
        """
        logger.info("A new thumbnail has been taken")
        # TODO Move this code outside from here
        temp_path = os.path.join(tempfile.gettempdir(), "tk-multi-support.jpg")
        pixmap.save(temp_path)
        self._report.thumbnails = [temp_path]  # TODO allows mutiple thumbs ?

    @QtCore.Slot()
    def on_text_edited(self, *args, **kwargs):
        """Called when the subject or the content field is edited. It enable
        or disable the send button.
        """
        if not self.lie_subject.text():
            self.pub_send.setEnabled(False)
            return
        if not self.txe_content.toPlainText():
            self.pub_send.setEnabled(False)
            return
        self.pub_send.setEnabled(True)
