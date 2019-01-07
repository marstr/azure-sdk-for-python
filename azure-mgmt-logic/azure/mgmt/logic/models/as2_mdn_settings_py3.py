# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AS2MdnSettings(Model):
    """The AS2 agreement mdn settings.

    All required parameters must be populated in order to send to Azure.

    :param need_mdn: Required. The value indicating whether to send or request
     a MDN.
    :type need_mdn: bool
    :param sign_mdn: Required. The value indicating whether the MDN needs to
     be signed or not.
    :type sign_mdn: bool
    :param send_mdn_asynchronously: Required. The value indicating whether to
     send the asynchronous MDN.
    :type send_mdn_asynchronously: bool
    :param receipt_delivery_url: The receipt delivery URL.
    :type receipt_delivery_url: str
    :param disposition_notification_to: The disposition notification to header
     value.
    :type disposition_notification_to: str
    :param sign_outbound_mdn_if_optional: Required. The value indicating
     whether to sign the outbound MDN if optional.
    :type sign_outbound_mdn_if_optional: bool
    :param mdn_text: The MDN text.
    :type mdn_text: str
    :param send_inbound_mdn_to_message_box: Required. The value indicating
     whether to send inbound MDN to message box.
    :type send_inbound_mdn_to_message_box: bool
    :param mic_hashing_algorithm: Required. The signing or hashing algorithm.
     Possible values include: 'NotSpecified', 'None', 'MD5', 'SHA1', 'SHA2256',
     'SHA2384', 'SHA2512'
    :type mic_hashing_algorithm: str or
     ~azure.mgmt.logic.models.HashingAlgorithm
    """

    _validation = {
        'need_mdn': {'required': True},
        'sign_mdn': {'required': True},
        'send_mdn_asynchronously': {'required': True},
        'sign_outbound_mdn_if_optional': {'required': True},
        'send_inbound_mdn_to_message_box': {'required': True},
        'mic_hashing_algorithm': {'required': True},
    }

    _attribute_map = {
        'need_mdn': {'key': 'needMdn', 'type': 'bool'},
        'sign_mdn': {'key': 'signMdn', 'type': 'bool'},
        'send_mdn_asynchronously': {'key': 'sendMdnAsynchronously', 'type': 'bool'},
        'receipt_delivery_url': {'key': 'receiptDeliveryUrl', 'type': 'str'},
        'disposition_notification_to': {'key': 'dispositionNotificationTo', 'type': 'str'},
        'sign_outbound_mdn_if_optional': {'key': 'signOutboundMdnIfOptional', 'type': 'bool'},
        'mdn_text': {'key': 'mdnText', 'type': 'str'},
        'send_inbound_mdn_to_message_box': {'key': 'sendInboundMdnToMessageBox', 'type': 'bool'},
        'mic_hashing_algorithm': {'key': 'micHashingAlgorithm', 'type': 'str'},
    }

    def __init__(self, *, need_mdn: bool, sign_mdn: bool, send_mdn_asynchronously: bool, sign_outbound_mdn_if_optional: bool, send_inbound_mdn_to_message_box: bool, mic_hashing_algorithm, receipt_delivery_url: str=None, disposition_notification_to: str=None, mdn_text: str=None, **kwargs) -> None:
        super(AS2MdnSettings, self).__init__(**kwargs)
        self.need_mdn = need_mdn
        self.sign_mdn = sign_mdn
        self.send_mdn_asynchronously = send_mdn_asynchronously
        self.receipt_delivery_url = receipt_delivery_url
        self.disposition_notification_to = disposition_notification_to
        self.sign_outbound_mdn_if_optional = sign_outbound_mdn_if_optional
        self.mdn_text = mdn_text
        self.send_inbound_mdn_to_message_box = send_inbound_mdn_to_message_box
        self.mic_hashing_algorithm = mic_hashing_algorithm
