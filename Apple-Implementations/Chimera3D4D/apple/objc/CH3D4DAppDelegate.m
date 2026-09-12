#import "CH3D4DAppDelegate.h"
#import "CH3D4DViewport.h"

@implementation CH3D4DAppDelegate
- (void)applicationDidFinishLaunching:(NSNotification *)notification {
    (void)notification;
    self.window = [[NSWindow alloc] initWithContentRect:NSMakeRect(0, 0, 1280, 800)
                                              styleMask:(NSWindowStyleMaskTitled | NSWindowStyleMaskClosable | NSWindowStyleMaskResizable)
                                                backing:NSBackingStoreBuffered
                                                  defer:NO];
    self.window.title = @"Chimera 3D/4D Studio";
    self.window.contentView = [[CH3D4DViewport alloc] initWithFrame:self.window.contentView.bounds];
    [self.window center];
    [self.window makeKeyAndOrderFront:nil];
}
@end
