#import "CH3D4DAppDelegate.h"
#import "CH3D4DViewport.h"
@implementation CH3D4DAppDelegate
- (void)applicationDidFinishLaunching:(NSNotification *)notification {
    NSWindow *window = [[NSWindow alloc] initWithContentRect:NSMakeRect(0,0,1280,800) styleMask:(NSWindowStyleMaskTitled|NSWindowStyleMaskClosable|NSWindowStyleMaskResizable) backing:NSBackingStoreBuffered defer:NO];
    window.title = @"Chimera 3D/4D Studio";
    window.contentView = [[CH3D4DViewport alloc] initWithFrame:window.contentView.bounds];
    [window makeKeyAndOrderFront:nil];
}
@end
