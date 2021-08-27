from linebot.models import (FlexSendMessage)
from typing import Optional


def flex_notify_channel(channel: str, date_time: str, company: str, name: str, tel: str, email: str, product: str,
                        message: str):
    flex_msg = FlexSendMessage(
        alt_text='Notify! customer contact',
        contents={
            "type": "bubble",
            "direction": "ltr",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": channel,
                                "size": "sm",
                                "color": "#AAAAAA",
                                "flex": 1,
                                "align": "start",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": date_time,
                                "size": "sm",
                                "color": "#666666",
                                "flex": 3,
                                "align": "end",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "กรุณาติดต่อกลับ",
                        "weight": "bold",
                        "size": "lg",
                        "margin": "md",
                        "contents": []
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "margin": "lg",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "บริษัท",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": company,
                                        "size": "sm",
                                        "color": "#666666",
                                        "flex": 5,
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ติดต่อ",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": name,
                                        "size": "sm",
                                        "color": "#666666",
                                        "flex": 5,
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "โทร.",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": tel,
                                        "size": "sm",
                                        "color": "#666666",
                                        "flex": 5,
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": email,
                                        "size": "sm",
                                        "color": "#666666",
                                        "flex": 5,
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สนใจ",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": product,
                                        "size": "sm",
                                        "color": "#666666",
                                        "flex": 5,
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "md"
                            },
                            {
                                "type": "text",
                                "text": "รายละเอียดเพิ่มเติม",
                                "size": "sm",
                                "color": "#AAAAAA",
                                "margin": "md",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": message,
                                "size": "sm",
                                "color": "#666666",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                ]
            }
        }
    )
    return flex_msg


def person_team_one():
    flex_message = FlexSendMessage(
        alt_text='นามบัตรทีมหนึ่ง',
        contents={
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://www.img.in.th/images/d4cafbf94c2f0e0a3bb9e3c51cdf8685.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                    "type": "postback",
                    "label": "action",
                    "data": "hello"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "บริษัทแมงโก้ คอนซัลแตนท์ จำกัด ",
                        "weight": "bold",
                        "size": "md",
                        "wrap": True,
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "555 อาคารรสา ทาวเวอร์ 1 ยูนิต 2304-1 ชั้น 23 ถ.พหลโยธิน แขวงจตุจักร เขตจตุจักร กรุงเทพฯ 10900 Call Center.02-123-3900 ",
                        "size": "xs",
                        "wrap": True,
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "เลขประจำตัวผู้เสียภาษี 0105551067687 ",
                        "size": "sm",
                        "wrap": True,
                        "contents": []
                    },
                    {
                        "type": "separator",
                        "margin": "xl"
                    },
                    {
                        "type": "text",
                        "text": "คุณอัญชลี  วงศ์พินทุ",
                        "weight": "bold",
                        "size": "lg",
                        "margin": "lg",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "Anchalee Wongpintu ",
                        "margin": "none",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "(Sales Manager)",
                        "size": "sm",
                        "margin": "xs",
                        "contents": []
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "margin": "lg",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Mobile",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "084-551-1044",
                                        "size": "sm",
                                        "color": "#3442E6FF",
                                        "flex": 5,
                                        "wrap": True,
                                        "contents": [],
                                        "action": {
                                            "type": "postback",
                                            "label": "action",
                                            "data": "team1_tel1"
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "anchalee@mangoconsultant.com",
                                        "size": "sm",
                                        "color": "#666666",
                                        "flex": 5,
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xl"
                            }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "คุณชัยชนะ ศรีปิ่นเป้า ",
                        "weight": "bold",
                        "size": "lg",
                        "margin": "md",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "Chaichana Serpinpao",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "(Sales Coordinator)",
                        "size": "sm",
                        "contents": []
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "margin": "lg",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Mobile",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": " 084-016-8454",
                                        "size": "sm",
                                        "color": "#3442E6FF",
                                        "flex": 5,
                                        "wrap": True,
                                        "contents": [],
                                        "action": {
                                            "type": "postback",
                                            "label": "action",
                                            "data": "team1_tel2"
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "Chaichana@mangoconsultant.com",
                                        "size": "sm",
                                        "color": "#666666",
                                        "flex": 6,
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xl"
                            },
                            {
                                "type": "text",
                                "text": "www.mangoconsultant.com",
                                "size": "sm",
                                "color": "#999999",
                                "align": "center",
                                "margin": "lg",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                ]
            }
        }
    )
    return flex_message


def person_team_two():
    flex_message = FlexSendMessage(
        alt_text='นามบัตรทีมสอง',
        contents={
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://www.img.in.th/images/d4cafbf94c2f0e0a3bb9e3c51cdf8685.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://www.img.in.th/images/d4cafbf94c2f0e0a3bb9e3c51cdf8685.png"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "บริษัทแมงโก้ คอนซัลแตนท์ จำกัด ",
                        "weight": "bold",
                        "size": "md",
                        "wrap": True,
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "555 อาคารรสา ทาวเวอร์ 1 ยูนิต 2304-1 ชั้น 23 ถ.พหลโยธิน แขวงจตุจักร เขตจตุจักร กรุงเทพฯ 10900 Call Center.02-123-3900 ",
                        "size": "xs",
                        "wrap": True,
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "เลขประจำตัวผู้เสียภาษี 0105551067687 ",
                        "size": "sm",
                        "wrap": True,
                        "contents": []
                    },
                    {
                        "type": "separator",
                        "margin": "xl"
                    },
                    {
                        "type": "text",
                        "text": "คุณริญญภัสร์ ปิยเดชไพบูลย์",
                        "weight": "bold",
                        "size": "lg",
                        "margin": "lg",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "Rinyaphas Piyadechaibul",
                        "margin": "none",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "(Sales Executive)",
                        "size": "sm",
                        "margin": "xs",
                        "contents": []
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "margin": "lg",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Mobile",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "086-956-5929",
                                        "size": "sm",
                                        "color": "#3442E6FF",
                                        "flex": 5,
                                        "wrap": True,
                                        "action": {
                                            "type": "postback",
                                            "label": "action",
                                            "data": "team2_tel1"
                                        },
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "rinyaphas@mangoconsultant.com",
                                        "size": "sm",
                                        "color": "#666666",
                                        "flex": 5,
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xl"
                            }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "คุณศุภกฤต  สมสาย",
                        "weight": "bold",
                        "size": "lg",
                        "margin": "md",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "Suppakrit  Somsai",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "(Key Account Executive)",
                        "size": "sm",
                        "contents": []
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "margin": "lg",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Mobile",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": " 098-828-5742",
                                        "size": "sm",
                                        "color": "#3442E6FF",
                                        "flex": 5,
                                        "wrap": True,
                                        "action": {
                                            "type": "postback",
                                            "label": "action",
                                            "data": "team2_tel2"
                                        },
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email",
                                        "size": "sm",
                                        "color": "#AAAAAA",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "suppakrit@mangoconsultant.com",
                                        "size": "sm",
                                        "color": "#666666",
                                        "flex": 6,
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xl"
                            },
                            {
                                "type": "text",
                                "text": "www.mangoconsultant.com",
                                "size": "sm",
                                "color": "#999999",
                                "align": "center",
                                "margin": "lg",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                ]
            }
        }
    )
    return flex_message


def erpSoftware():
    flex_message = FlexSendMessage(
        alt_text='ERPSoftWare',
        contents={"type": "carousel",
                  "contents": [
                      {
                          "type": "bubble",
                          "hero": {
                              "type": "image",
                              "url": "https://sv1.picz.in.th/images/2020/10/08/OLdApf.png",
                              "size": "full"
                          },
                          "body": {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                  {
                                      "type": "text",
                                      "text": "ราคามีทั้งแบบซื้อและแบบเช่ารายเดือน",
                                      "size": "md",
                                      "color": "#ffffff",
                                      "weight": "bold"
                                  },
                                  {
                                      "type": "text",
                                      "text": "ขึ้นอยู่กับ Package และจำนวน User ที่ต้องการ",
                                      "size": "xs",
                                      "color": "#ffffff",
                                      "weight": "bold"
                                  },
                                  {
                                      "type": "text",
                                      "text": "ใช้งาน โดยราคาเริ่มตั้งแต่หลักหมื่น",
                                      "size": "xs",
                                      "color": "#ffffff",
                                      "weight": "bold"
                                  }
                              ],
                              "backgroundColor": "#008891"
                          },
                          "footer": {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                  {
                                      "type": "box",
                                      "layout": "vertical",
                                      "contents": [
                                          {
                                              "type": "filler"
                                          },
                                          {
                                              "type": "box",
                                              "layout": "baseline",
                                              "contents": [
                                                  {
                                                      "type": "filler"
                                                  },
                                                  {
                                                      "type": "text",
                                                      "text": "ข้อมูลเพิ่มเติม",
                                                      "color": "#ffffff",
                                                      "size": "lg",
                                                      "flex": 0
                                                  },
                                                  {
                                                      "type": "filler"
                                                  }
                                              ],
                                              "action": {
                                                  "type": "uri",
                                                  "label": "action",
                                                  "uri": "https://www.mangoconsultant.com/th/mango-anywhere-software/software-erp-for-construction-2"
                                              }
                                          },
                                          {
                                              "type": "filler"
                                          }
                                      ],
                                      "backgroundColor": "#008891",
                                      "spacing": "sm",
                                      "height": "35px",
                                      "borderWidth": "1px",
                                      "borderColor": "#ffffff",
                                      "flex": 0,
                                      "cornerRadius": "4px"
                                  },
                                  {
                                      "type": "box",
                                      "layout": "vertical",
                                      "contents": [
                                          {
                                              "type": "filler"
                                          },
                                          {
                                              "type": "box",
                                              "layout": "baseline",
                                              "contents": [
                                                  {
                                                      "type": "filler"
                                                  },
                                                  {
                                                      "type": "text",
                                                      "text": "ขอใบเสนอราคา",
                                                      "color": "#ffffff",
                                                      "size": "lg",
                                                      "flex": 0
                                                  },
                                                  {
                                                      "type": "filler"
                                                  }
                                              ],
                                              "action": {
                                                  "type": "uri",
                                                  "label": "action",
                                                  "uri": "https://liff.line.me/1655208213-8r59zjPv"
                                              }
                                          },
                                          {
                                              "type": "filler"
                                          }
                                      ],
                                      "backgroundColor": "#008891",
                                      "spacing": "sm",
                                      "height": "35px",
                                      "borderWidth": "1px",
                                      "borderColor": "#ffffff",
                                      "flex": 0,
                                      "cornerRadius": "4px",
                                      "margin": "md"
                                  }
                              ],
                              "backgroundColor": "#008891"
                          }
                      },
                      {
                          "type": "bubble",
                          "hero": {
                              "type": "image",
                              "url": "https://sv1.picz.in.th/images/2020/10/08/OLSzAy.png",
                              "size": "full"
                          },
                          "body": {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                  {
                                      "type": "text",
                                      "text": "ราคามีทั้งแบบซื้อและแบบเช่ารายเดือน",
                                      "size": "md",
                                      "color": "#ffffff",
                                      "weight": "bold"
                                  },
                                  {
                                      "type": "text",
                                      "text": "ขึ้นอยู่กับ Package และจำนวน User ที่ต้องการ",
                                      "size": "xs",
                                      "color": "#ffffff",
                                      "weight": "bold"
                                  },
                                  {
                                      "type": "text",
                                      "text": "ใช้งาน โดยราคาเริ่มตั้งแต่หลักหมื่น",
                                      "size": "xs",
                                      "weight": "bold",
                                      "color": "#ffffff"
                                  }
                              ],
                              "backgroundColor": "#008891"
                          },
                          "footer": {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                  {
                                      "type": "box",
                                      "layout": "vertical",
                                      "contents": [
                                          {
                                              "type": "filler"
                                          },
                                          {
                                              "type": "box",
                                              "layout": "baseline",
                                              "contents": [
                                                  {
                                                      "type": "filler"
                                                  },
                                                  {
                                                      "type": "text",
                                                      "text": "ข้อมูลเพิ่มเติม",
                                                      "color": "#ffffff",
                                                      "size": "lg",
                                                      "flex": 0
                                                  },
                                                  {
                                                      "type": "filler"
                                                  }
                                              ],
                                              "action": {
                                                  "type": "uri",
                                                  "label": "action",
                                                  "uri": "https://www.mangoconsultant.com/th/mango-anywhere-software/software-erp-for-real-estate"
                                              }
                                          },
                                          {
                                              "type": "filler"
                                          }
                                      ],
                                      "backgroundColor": "#008891",
                                      "spacing": "sm",
                                      "height": "35px",
                                      "borderWidth": "1px",
                                      "borderColor": "#ffffff",
                                      "cornerRadius": "4px",
                                      "flex": 0
                                  },
                                  {
                                      "type": "box",
                                      "layout": "vertical",
                                      "contents": [
                                          {
                                              "type": "filler"
                                          },
                                          {
                                              "type": "box",
                                              "layout": "baseline",
                                              "contents": [
                                                  {
                                                      "type": "filler"
                                                  },
                                                  {
                                                      "type": "text",
                                                      "text": "ขอใบเสนอราคา",
                                                      "color": "#ffffff",
                                                      "size": "lg",
                                                      "flex": 0,
                                                      "action": {
                                                          "type": "uri",
                                                          "label": "action",
                                                          "uri": "https://liff.line.me/1655208213-bR4352Oe"
                                                      }
                                                  },
                                                  {
                                                      "type": "filler"
                                                  }
                                              ],
                                              "action": {
                                                  "type": "uri",
                                                  "label": "action",
                                                  "uri": "https://liff.line.me/1655208213-bR4352Oe"
                                              }
                                          },
                                          {
                                              "type": "filler"
                                          }
                                      ],
                                      "backgroundColor": "#008891",
                                      "spacing": "sm",
                                      "height": "35px",
                                      "borderWidth": "1px",
                                      "borderColor": "#ffffff",
                                      "flex": 0,
                                      "cornerRadius": "4px",
                                      "margin": "md"
                                  }
                              ],
                              "backgroundColor": "#008891"
                          }
                      }
                  ]}
    )
    return flex_message
