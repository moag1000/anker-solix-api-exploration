// Excerpt of charging/http/http_request_repository_impl.dart (App 3.24.3): getMessage
// @0x297c340 and its success closure @0x297c628, copied from the Blutter asm; stack
// frame/overflow-check lines and write-barrier raw lines trimmed (118 lines).
class HttpRequestControllerImpl extends HttpRequestControllerInterface {
  _ getMessage(/* No info */) {
    // ** addr: 0x297c340, size: 0x234
    // 0x297c34c: SetupParameters(HttpRequestControllerImpl this /* r1 => r1, fp-0x8 */, dynamic _ /* r2 => r2, fp-0x10 */, dynamic _ /* r3 => r0, fp-0x18 */, dynamic _ /* r5 => r5, fp-0x20 */, dynamic _ /* r6 => r6, fp-0x28 */, dynamic _ /* r7 => r7, fp-0x30 */)
    // 0x297c374: r1 = 3
    // 0x297c378: r0 = AllocateContext()
    // 0x297c37c: mov             x3, x0
    // 0x297c380: ldur            x0, [fp, #-0x10]
    // 0x297c384: stur            x3, [fp, #-0x38]
    // 0x297c388: StoreField: r3->field_f = r0
    //     0x297c388: stur            w0, [x3, #0xf]
    // 0x297c38c: ldur            x0, [fp, #-0x20]
    // 0x297c390: StoreField: r3->field_13 = r0
    //     0x297c390: stur            w0, [x3, #0x13]
    // 0x297c394: ldr             x0, [fp, #0x10]
    // 0x297c398: ArrayStore: r3[0] = r0  ; List_4
    //     0x297c398: stur            w0, [x3, #0x17]
    // 0x297c39c: r1 = Null
    // 0x297c3a0: r2 = 20
    // 0x297c3a4: r0 = AllocateArray()
    // 0x297c3a8: mov             x2, x0
    // 0x297c3ac: r16 = "last_time"
    // 0x297c3b4: StoreField: r2->field_f = r16
    //     0x297c3b4: stur            w16, [x2, #0xf]
    // 0x297c3b8: ldur            x3, [fp, #-0x30]
    // 0x297c3bc: r0 = BoxInt64Instr(r3)
    // 0x297c3d0: mov             x1, x2
    // 0x297c3d4: ArrayStore: r1[1] = r0  ; List_4
    //     0x297c3d4: add             x25, x1, #0x13
    //     0x297c3d8: str             w0, [x25]
    // 0x297c3f8: r16 = "device_sns"
    // 0x297c400: ArrayStore: r2[0] = r16  ; List_4
    //     0x297c400: stur            w16, [x2, #0x17]
    // 0x297c404: mov             x1, x2
    // 0x297c408: ldur            x0, [fp, #-0x18]
    // 0x297c40c: ArrayStore: r1[3] = r0  ; List_4
    //     0x297c40c: add             x25, x1, #0x1b
    //     0x297c410: str             w0, [x25]
    // 0x297c430: r16 = "limit"
    // 0x297c438: StoreField: r2->field_1f = r16
    //     0x297c438: stur            w16, [x2, #0x1f]
    // 0x297c43c: r16 = 20
    // 0x297c440: StoreField: r2->field_23 = r16
    //     0x297c440: stur            w16, [x2, #0x23]
    // 0x297c444: r16 = "message_type"
    // 0x297c44c: StoreField: r2->field_27 = r16
    //     0x297c44c: stur            w16, [x2, #0x27]
    // 0x297c450: mov             x1, x2
    // 0x297c454: ldr             x0, [fp, #0x20]
    // 0x297c458: ArrayStore: r1[7] = r0  ; List_4
    //     0x297c458: add             x25, x1, #0x2b
    //     0x297c45c: str             w0, [x25]
    // 0x297c47c: r16 = "last_msg_id"
    // 0x297c484: StoreField: r2->field_2f = r16
    //     0x297c484: stur            w16, [x2, #0x2f]
    // 0x297c488: ldur            x3, [fp, #-0x28]
    // 0x297c48c: r0 = BoxInt64Instr(r3)
    // 0x297c4a0: mov             x1, x2
    // 0x297c4a4: ArrayStore: r1[9] = r0  ; List_4
    //     0x297c4a4: add             x25, x1, #0x33
    //     0x297c4a8: str             w0, [x25]
    // 0x297c4c8: r16 = <String, dynamic>
    // 0x297c4cc: stp             x2, x16, [SP]
    // 0x297c4d0: r0 = Map._fromLiteral()
    // 0x297c4d4: ldur            x2, [fp, #-0x38]
    // 0x297c4d8: r1 = Function '<anonymous closure>':.
    //     0x297c4d8: add             x1, PP, #0xc2, lsl #12  ; [pp+0xc2e80] AnonymousClosure: (0x297c628), in [package:charging/http/http_request_repository_impl.dart] HttpRequestControllerImpl::getMessage (0x297c340)
    // 0x297c4e0: stur            x0, [fp, #-0x10]
    // 0x297c4e4: r0 = AllocateClosure()
    // 0x297c4e8: ldur            x2, [fp, #-0x38]
    // 0x297c4ec: r1 = Function '<anonymous closure>':.
    // 0x297c4f4: stur            x0, [fp, #-0x18]
    // 0x297c4f8: r0 = AllocateClosure()
    // 0x297c4fc: ldur            x2, [fp, #-0x38]
    // 0x297c500: r1 = Function '<anonymous closure>':.
    // 0x297c508: stur            x0, [fp, #-0x20]
    // 0x297c50c: r0 = AllocateClosure()
    // 0x297c510: r16 = <Object?>
    // 0x297c514: ldur            lr, [fp, #-8]
    // 0x297c518: stp             lr, x16, [SP, #0x40]
    // 0x297c51c: r16 = Instance_Method
    //     0x297c51c: add             x16, PP, #0xa, lsl #12  ; [pp+0xa7e0] Obj!Method@4211741
    // 0x297c524: r30 = "/power_service/v1/get_message"
    // 0x297c52c: stp             lr, x16, [SP, #0x30]
    // 0x297c530: ldur            x16, [fp, #-0x10]
    // 0x297c534: ldur            lr, [fp, #-0x20]
    // 0x297c538: stp             lr, x16, [SP, #0x20]
    // 0x297c53c: ldur            x16, [fp, #-0x18]
    // 0x297c540: r30 = false
    // 0x297c544: stp             lr, x16, [SP, #0x10]
    // 0x297c548: ldr             x16, [fp, #0x18]
    // 0x297c54c: stp             x0, x16, [SP]
    // 0x297c550: r4 = const [0x1, 0x9, 0x9, 0x6, complete, 0x8, isLogResponse, 0x6, showLoading, 0x7, null]
    // 0x297c558: r0 = encryptionRequestHttp()
    // 0x297c55c: r0 = Null
    // 0x297c570: b               #0x297c374
  }
  [closure] Null <anonymous closure>(dynamic, Object?) {
    // ** addr: 0x297c628, size: 0x88
    // 0x297c634: SetupParameters()
    // 0x297c650: r1 = "---> getMessage request success"
    // 0x297c658: r4 = const [0, 0x1, 0, 0x1, null]
    // 0x297c65c: r0 = exeSuccess()
    // 0x297c660: r0 = MsgHttpModel()
    // 0x297c664: mov             x1, x0
    // 0x297c668: ldr             x2, [fp, #0x10]
    // 0x297c66c: stur            x0, [fp, #-0x10]
    // 0x297c670: r0 = MsgHttpModel.fromJson()
    // 0x297c674: ldur            x0, [fp, #-8]
    // 0x297c678: ArrayLoad: r1 = r0[0]  ; List_4
    // 0x297c67c: DecompressPointer r1
    // 0x297c680: ldur            x16, [fp, #-0x10]
    // 0x297c684: stp             x16, x1, [SP]
    // 0x297c688: mov             x0, x1
    // 0x297c68c: ClosureCall
    // 0x297c698: r0 = Null
    // 0x297c6ac: b               #0x297c650
  }
// SYNTHETIC (not from the app): the function below exists only for the tests.
  _ synthBuilder(/* No info */) {
    // ** addr: 0x1000, size: 0x100
    // 0x1004: SetupParameters(Synth this /* r1 => r1, fp-0x8 */, dynamic _ /* r2 => r2, fp-0x10 */)
    // 0x1008: r1 = Null
    // 0x100c: r2 = 8
    // 0x1010: r0 = AllocateArray()
    // 0x1014: mov             x2, x0
    // 0x1018: r16 = "flag"
    // 0x101c: StoreField: r2->field_f = r16
    //     0x101c: stur            w16, [x2, #0xf]
    // 0x1020: r16 = true
    // 0x1024: StoreField: r2->field_13 = r16
    //     0x1024: stur            w16, [x2, #0x13]
    // 0x1028: r16 = "big"
    // 0x102c: StoreField: r2->field_17 = r16
    //     0x102c: stur            w16, [x2, #0x17]
    // 0x1030: r3 = 12345
    // 0x1034: r0 = BoxInt64Instr(r3)
    // 0x1038: mov             x1, x2
    // 0x103c: ArrayStore: r1[3] = r0  ; List_4
    //     0x103c: stur            w0, [x1, #0x1b]
    // 0x1040: r16 = <String, dynamic>
    // 0x1044: stp             x2, x16, [SP]
    // 0x1048: r0 = Map._fromLiteral()
    // 0x104c: mov             x3, x0
    // 0x1050: ldur            x0, [fp, #-0x10]
    // 0x1054: stur            x3, [fp, #-0x18]
    // 0x1058: cmp             w0, NULL
    // 0x105c: b.eq            #0x1090
    // 0x1060: r2 = "opt"
    // 0x1064: ldur            x1, [fp, #-0x18]
    // 0x1068: mov             x3, x0
    // 0x106c: r0 = GDT[cid_x0 + 0x6a9]()
    // 0x1090: r0 = Null
  }
// SYNTHETIC: Smi built from an int parameter (ldur + lsl); `r2 = 4` is only the
// AllocateArray size and must never become the value (review finding C1/I1).
  _ synthLsl(/* No info */) {
    // ** addr: 0x2000, size: 0x100
    // 0x2004: SetupParameters(Synth this /* r1 => r1, fp-0x8 */, dynamic _ /* r2 => r2, fp-0x28 */)
    // 0x2008: r1 = Null
    // 0x200c: r2 = 4
    // 0x2010: r0 = AllocateArray()
    // 0x2014: r16 = "type"
    // 0x2018: StoreField: r0->field_f = r16
    //     0x2018: stur            w16, [x0, #0xf]
    // 0x201c: ldur            x1, [fp, #-0x28]
    // 0x2020: lsl             x2, x1, #1
    // 0x2024: StoreField: r0->field_13 = r2
    //     0x2024: stur            w2, [x0, #0x13]
    // 0x2028: stur            x0, [fp, #-0x30]
    // 0x202c: r16 = <String, dynamic>
    // 0x2030: ldur            lr, [fp, #-0x30]
    // 0x2034: stp             lr, x16, [SP]
    // 0x2038: r0 = Map._fromLiteral()
  }
// SYNTHETIC: builder without a map literal and its direct caller with {type_id: 1}.
  _ synthNoMap(/* No info */) {
    // ** addr: 0x3000, size: 0x40
    // 0x3004: SetupParameters(Synth this /* r1 => r1, fp-0x8 */, dynamic _ /* r2 => r2, fp-0x10 */)
    // 0x3008: r30 = "/power_service/v1/synth/no_map"
    // 0x300c: r0 = encryptionRequestHttp()
  }
  _ synthCaller(/* No info */) {
    // ** addr: 0x4000, size: 0x80
    // 0x4004: r1 = Null
    // 0x4008: r2 = 4
    // 0x400c: r0 = AllocateArray()
    // 0x4010: mov             x2, x0
    // 0x4014: r16 = "type_id"
    // 0x4018: StoreField: r2->field_f = r16
    //     0x4018: stur            w16, [x2, #0xf]
    // 0x401c: r16 = 2
    // 0x4020: StoreField: r2->field_13 = r16
    //     0x4020: stur            w16, [x2, #0x13]
    // 0x4024: r16 = <String, dynamic>
    // 0x4028: stp             x2, x16, [SP]
    // 0x402c: r0 = Map._fromLiteral()
    // 0x4030: r0 = synthNoMap()
  }
