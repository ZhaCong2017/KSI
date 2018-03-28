

区块链平台接口
=================================================================
// 资产增删改  

    url:  http://ip:port/bloack_chain/property_invoke

    req:
        {
            "invoke_type":  (int    操作类型),  // 012 - 增删改
            "property_id":  (string 资产id),
            "owner":        (string 归属者)    // 当删除的时候，填字符串"NULL"
        }

    rsp:
        {
            "result_code":  (int     结果码),  // 成功为0；其他为失败
            "result_desc":  (string  结果描述)  // 结果码描述
            "data":         (object)            // 失败时填空
                {
                    "transaction_id":   (String fabric交易id)
                }
        }


------------------------------------------------------------
// 资产查 

    url:  http://ip:port/bloack_chain/property_query

    req:
        {
            "property_id":  (string  资产id)
        }

    rsp:
        {
            "result_code":  (sint     结果码),      // 成功为0；其他为失败
            "result_desc":  (sstring  结果描述),    // 结果码描述
            "data":         (object)
                {
                    "owner":   (String 归属者)
                }
        }


------------------------------------------------------------
// 区块链信息查询 

    url:  http://ip:port/bloack_chain/block_chain_info

    req:

    rsp:
        {
            "result_code":  (int     结果码),       // 成功为0；其他为失败
            "result_desc":  (string  结果描述),     // 结果码描述
            "data":         (object)
                {
                    "block_chain_height":   (int 区块高度)
                    "transaction_count":    (int 交易记录数)
                }
        }


------------------------------------------------------------
// 区块链平台节点信息查询  

    url:  http://ip:port/bloack_chain/node_info

    req:
        {
            "node_id_list":     (array  节点id列表)     // []传空时表示查询所有
                [
                    "node_id":  (string 节点id),
                    ...
                ]
        }

    rsp:
        {
            "result_code":          int     结果码,         // 成功为0；其他为失败
            "result_desc":          string  结果描述        // 结果码描述
            "data":                 (object)
                {
                    "node_list":    
                        [
                            {
                                "n_id":         (string 节点id),
                                "n_online":     (int 节点是否在线),
                                "n_type":       (string 节点类型：order，peer，ca-server),
                                "n_group":      (string 节点归属组：ksi，xmf，cdn),
                                "n_ip":         (string 节点ip),
                                "n_area":       (string 节点区域),
                                "n_isp":        (string 节点运营商),
                                "n_os":         (string 节点系统)
                            },
                            ...
                        ]
                }
        }


------------------------------------------------------------
// 区块链平台节点状态信息查询 

    url:  http://ip:port/bloack_chain/node_stat

    req:
        {
            "node_id_list":     (array  节点id列表)     // []传空时表示查询所有
                [
                    "node_id":  (string 节点id)
                ]
        }

    rsp:
        {
            "result_code":          int     结果码,         // 成功为0；其他为失败
            "result_desc":          string  结果描述        // 结果码描述
            "data":                 (object)
                {
                    "node_list":    
                        [
                            {
                                "n_id":             (string 节点id),
                                "cpu_useage":       (int 百分比),
                                "mem_useage":       (int 百分比),
                                "io_useage":        (int blocks num)
                            },
                            ......
                        ]
                }
        }


------------------------------------------------------------
// 区块链平台节点上下线  -- 赵国华

    url:  http://ip:port/bloack_chain/node_up_down

    req:
        {
            "node_operate_list":     (array  节点列表)     // []传空时不作任何处理
                [
                    {
                        "n_id":     (string 节点id),
                        "op_type":  (int    0:down;1:up)
                    },
                    ......
                ]
        }

    rsp:
        {
            "result_code":          int     结果码,         // 成功为0；其他为失败(这里只要不是系统错误就返回成功)
            "result_desc":          string  结果描述        // 结果码描述
            "data":                 (object)
                {
                    "node_list":    
                        [
                            {
                                "n_id":             (string 节点id),
                                "op_type":          (int    0:down; 1:up),
                                "op_result":        (int    0:succ; other:failed),
                                "op_desc":          (string op_result描述),
                            },
                            ......
                        ]
                }
        }

------------------------------------------------------------
// 区块链平台资产签名验签tps测试任务创建接口  

    url:  http://ip:port/bloack_chain/test_task_create

    req:
        {
            "tps_test_type":  (int 0:签名;1:验签)
        }

    rsp:
        {
            "result_code":          int     结果码,         // 成功为0；其他为失败
            "result_desc":          string  结果描述        // 结果码描述
            "data":                 (object)
                {
                    "task_id":   (string 测试任务id)
                }
        }

------------------------------------------------------------
// 区块链平台根据测试任务查询测试记录  

    url:  http://ip:port/bloack_chain/test_task_record

    req:
        {
            "task_id":          (int 测试任务id),
            "last_record_id":   (int 第一次查询传0；后续查询传最后一条记录的record_id)  // 用来增量返回记录
        }

    rsp:
        {
            "result_code":          int     结果码,         // 成功为0；其他为失败
            "result_desc":          string  结果描述        // 结果码描述
            "data":                 (object)
                {
                    "record_list":   (array)
                        [
                            {
                                "record_id":    (int 记录id),
                                "report_time":  (string 记录上报时间),
                                "tps":          (int tps),
								"rsp_avg_time": (long 平均响应时间)
                            },
                            ......
                        ]
                }
        }


------------------------------------------------------------
// 区块链平台资产区块链逻辑树查询接口  

    url:  http://ip:port/bloack_chain/block_hash_tree_for_property

    req:
        {
            "property_id":  (string 资产id)
        }

    rsp:
        {
            "result_code":          int     结果码,         // 成功为0；其他为失败
            "result_desc":          string  结果描述        // 结果码描述
            "data":                 (object)
                {
                    "block_hash_tree":      (array)
                        [
                            {
                                "idx":          (long 按资产第一次出现的区块到最后一次出现的区块排序)
                                "root_hash":    (string 区块根hash)
                                "pre_root_hash":(string 前一个区块的根hash)
                                "tx_id":        (string 交易编号)
                                "tx_idx"":      (int 交易在本区块的索引号)
                                "property_id":  (string 本笔交易所涉及到的资产编号)
                            },
                            ......
                        ]
                }
        }

------------------------------------------------------------
